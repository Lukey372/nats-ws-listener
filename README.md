# NATS WebSocket Listener

This project is a Python-based WebSocket listener that connects to a NATS server via a WebSocket endpoint (`wss://prod-v2.nats.realtime.pump.fun/`). The script authenticates with the server, subscribes to the `newCoinCreated.prod` channel, and processes incoming messages. It also sends periodic keepalive PING messages to maintain the connection.

## Features

- Connects to a WebSocket endpoint using the `websockets` library.
- Sends periodic keepalive messages.
- Authenticates with a NATS server using a CONNECT command.
- Subscribes to a specific channel (`newCoinCreated.prod`).
- Logs and processes incoming messages.

## Prerequisites

- Python 3.7 or higher
- The `websockets` package (see [requirements.txt](requirements.txt))

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd nats-ws-listener
