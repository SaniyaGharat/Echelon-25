import { QueryClient, QueryFunction } from "@tanstack/react-query";

async function throwIfResNotOk(res: Response) {
    if (!res.ok) {
        const text = (await res.text()) || res.statusText;
        throw new Error(`${res.status}: ${text}`);
    }
}

export async function apiRequest(method: string, url: string, data?: unknown): Promise<Response> {
    const res = await fetch(url, {
        method,
        headers: data ? { "Content-Type": "application/json" } : {},
        body: data ? JSON.stringify(data) : undefined,
        credentials: "include",
    });

    await throwIfResNotOk(res);
    return res;
}

export const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            queryFn: async ({ queryKey }) => {
                const res = await fetch(queryKey[0] as string, { credentials: "include" });
                await throwIfResNotOk(res);
                return await res.json();
            },
            refetchOnWindowFocus: false,
            staleTime: Infinity,
            retry: false,
        },
    },
});
