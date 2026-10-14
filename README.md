# AI-Assisted Security Operations Center (SOC)

## Overview

This project aims to develop an AI-assisted Security Operations Center (SOC) that collects security telemetry, analyzes events, identifies potentially malicious activity, and helps analysts investigate security alerts.

The system will combine rule-based detection with AI-assisted analysis to support security monitoring and investigation.

**Project status:** Early development — foundational backend setup.

## Planned Features

- **Endpoint telemetry:** Collect relevant security events from monitored systems.
- **Centralized log ingestion:** Receive and process structured security events through an API.
- **Threat detection:** Identify suspicious activity using deterministic detection rules, with potential anomaly detection capabilities.
- **Alert management:** Store, organize, and investigate security alerts.
- **AI-assisted analysis:** Provide contextual explanations and investigation support for selected security events.

These are planned capabilities and are not yet implemented unless explicitly documented as complete.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- Git and GitHub

Additional technologies will be documented as the architecture develops.

## Current Progress

- Initial FastAPI application created.
- Health-check endpoint implemented.
- Git repository and `.gitignore` configured.
- PostgreSQL development environment prepared; application integration is in progress.

## Development Workflow

Development takes place on feature branches. Changes are submitted through pull requests and reviewed before being merged into `main`.

## Project Structure

The repository structure will evolve as backend modules, endpoint agents, detection components, tests, and documentation are introduced.
