## mcp-hello (Cloudflare Workers MCP Server)

TypeScript implementation of an MCP server running on Cloudflare Workers using the `workers-mcp` library. It exposes two simple tools backed by class methods:

| Tool | Description | Parameters |
|------|-------------|------------|
| `sayHello` | Returns a friendly greeting. | name (string) |
| `getCurrentTime` | Current ISO timestamp with optional message. | message? (string) |

---

## Quick Start
Prerequisites: Node.js 18+, `pnpm` (or npm / yarn) & a Cloudflare account (for deploy).

```powershell
cd mcp-hello
pnpm install        # (or npm install)
pnpm dev            # Wrangler development server
```

Wrangler will print a local preview URL. The MCP endpoints are auto-routed through the worker (the `ProxyToSelf` handles dispatch).

---

## Project Structure
| File | Purpose |
|------|---------|
| `src/index.ts` | Worker entry – defines class with MCP-exposed methods. |
| `wrangler.jsonc` | Worker configuration (name, main script, compatibility date). |
| `worker-configuration.d.ts` | Type support for environment bindings. |
| `vitest.config.mts` | Test runner config. |
| `test/index.spec.ts` | Example test (extend with tool tests). |

---

## Scripts
| Command | Action |
|---------|--------|
| `pnpm dev` | Run local dev worker. |
| `pnpm test` | Execute Vitest tests. |
| `pnpm deploy` | Generate docs (`workers-mcp docgen`) then deploy via Wrangler. |
| `pnpm cf-typegen` | Refresh Cloudflare type bindings. |

---

## Adding Tools
Add a new instance method to the exported `WorkerEntrypoint` subclass. Include JSDoc comments – `workers-mcp docgen` can extract metadata for clients.

```ts
myFancyOp(value: number) {
  return value * 2
}
```

Run:
```powershell
pnpm deploy
```
to regenerate docs & deploy.

---

## Local Testing Idea
Use an MCP client that can target the worker URL once deployed. (Workers currently serve HTTP endpoints suitable for bridging by `workers-mcp`; consult its docs for exact client wiring.)

Example pseudo-call (after wrapping in a generic MCP HTTP client):
```jsonc
{
  "method": "sayHello",
  "params": { "name": "Dev" }
}
```

---

## Deployment
1. Authenticate Wrangler (`wrangler login`).
2. Ensure `wrangler.jsonc` name is unique in your account.
3. Deploy:
```powershell
pnpm deploy
```
4. Note the production URL -> configure your MCP client to point at it.

---

## Roadmap Ideas
* Add streaming tool outputs.
* Persist state via KV / D1 / R2 bindings.
* Authentication / rate limiting.

---

## License
MIT (placeholder).

---

## Contributing
PRs welcome – add tests for any new tools.
