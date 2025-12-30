# Dockerfile for Prompt Engineering Lab MCP Server
# Author: Anderson Henrique da Silva
# Location: Minas Gerais, Brazil
#
# Build: docker build -t prompt-engineering-mcp .
# Run:   docker run -p 8000:8000 -e MCP_MODE=remote prompt-engineering-mcp

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MCP_MODE=remote \
    MCP_PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p evidence/metrics/data \
    evidence/metrics/reports \
    evidence/models \
    evidence/patterns \
    evidence/antipatterns \
    experiments/hypothesis \
    experiments/results

# Expose port for SSE transport
EXPOSE 8000

# Run the MCP server
CMD ["python", "mcp_server.py"]
