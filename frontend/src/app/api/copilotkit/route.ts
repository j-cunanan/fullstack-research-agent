import {
    CopilotRuntime,
    OpenAIAdapter,
    copilotRuntimeNextJSAppRouterEndpoint,
    langGraphPlatformEndpoint,
} from '@copilotkit/runtime';
import OpenAI from 'openai';
import { NextRequest } from 'next/server';

// const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const instance = "jayso-m86ldqty-eastus2";
const model = "gpt-4o-mini";

const apiKey = process.env["AZURE_OPENAI_API_KEY"];
if (!apiKey) {
    throw new Error("The AZURE_OPENAI_API_KEY environment variable is missing or empty.");
}

const openai = new OpenAI({
    apiKey,
    baseURL: `https://${instance}.cognitiveservices.azure.com/openai/deployments/${model}`,
    defaultQuery: { "api-version": "2024-12-01-preview" },
    defaultHeaders: { "api-key": apiKey },
});
const serviceAdapter = new OpenAIAdapter({ openai });
const deploymentUrl = process.env.DEPLOYMENT === 'local' ? process.env.LOCAL_DEPLOYMENT_URL : process.env.DEPLOYMENT_URL
const runtime = new CopilotRuntime({
    remoteEndpoints: [
        langGraphPlatformEndpoint({
            deploymentUrl: deploymentUrl!,
            langsmithApiKey: process.env.LANGSMITH_API_KEY!,
            agents: [{
                name: 'agent',
                description: 'Research assistant',
            }],
        })
    ]
});

export const POST = async (req: NextRequest) => {
    const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
        runtime,
        serviceAdapter,
        endpoint: '/api/copilotkit',
    });

    return handleRequest(req);
};