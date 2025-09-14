import { WorkerEntrypoint } from 'cloudflare:workers'
import { ProxyToSelf } from 'workers-mcp'

export default class MyWorker extends WorkerEntrypoint<Env> {
  /**
   * A warm, friendly greeting from your new Workers MCP server.
   * @param name {string} the name of the person we are greeting.
   * @return {string} the contents of our greeting.
   */
  sayHello(name: string) {
    return `Hello from an MCP Worker, ${name}!`
  }

  /**
   * Gets the current time with a custom message
   * @param message {string} optional custom message to include
   * @return {string} formatted timestamp with message
   */
  getCurrentTime(message?: string) {
    const timestamp = new Date().toISOString()
    return message
      ? `${message} at ${timestamp}`
      : `Current time is ${timestamp}`
  }

  /**
   * @ignore
   **/
  async fetch(request: Request): Promise<Response> {
    return new ProxyToSelf(this).fetch(request)
  }
}
