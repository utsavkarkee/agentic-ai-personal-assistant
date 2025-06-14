# Agentic AI Personal Assistant

An intelligent personal assistant built with Langchain that learns your preferences, manages your tasks, provides contextual reminders, and integrates with your calendar.

## 🎯 Project Overview

This project aims to build a comprehensive personal AI assistant that:
- Learns work habits, communication style, preferences (food, music, products) through conversations
- Manages todo lists and shopping lists with natural language input
- Provides intelligent reminders for work deadlines, health, water intake, and errands
- Maintains conversation context and personal preferences across sessions
- Integrates with Google Calendar (read/write) for scheduling and meeting preparation
- Offers a modern, responsive web interface built with Next.js
- Deploys on AWS with a simple but scalable architecture

## 🏗️ Architecture

### Core Components
- **AI Agent**: Langchain-powered conversational agent
- **Memory System**: Long-term storage of preferences and context
- **Task Manager**: Todo and shopping list management
- **Reminder Engine**: Intelligent notification system
- **Calendar Integration**: Google Calendar/Outlook integration
- **Web Interface**: Modern React-based UI
- **API Backend**: FastAPI/Flask REST API

### Tech Stack

#### **Phase 1: Traditional Architecture (MVP)**
- **Backend**: Python, Langchain, FastAPI
- **Database**: SQLite (dev) → PostgreSQL (production)
- **AI/ML**: OpenAI GPT-4, Langchain agents with direct tool integration
- **Frontend**: Next.js, React, TypeScript, Tailwind CSS
- **Calendar**: Google Calendar API (direct integration)
- **Deployment**: AWS (EC2, RDS, S3, CloudFront)
- **Infrastructure**: Docker

#### **Phase 2: MCP Migration (Future Enhancement)**
- **Protocol**: Model Context Protocol (MCP) for standardized AI-service integration
- **Architecture**: Three-tier (AI Client ↔ MCP Server ↔ Resources)
- **Benefits**: Enhanced security, tool composability, third-party integrations
- **Migration**: Gradual refactoring of direct integrations to MCP resources/tools

## 📋 Development Checklist

### Phase 1: Project Setup & Foundation ✅ COMPLETED
- [x] Initialize project structure
- [x] Set up Python virtual environment  
- [x] Install core dependencies (Langchain, FastAPI, etc.)
- [x] Set up database schema design (User, Task, Conversation models)
- [x] Create basic FastAPI server with lifespan management
- [x] Set up environment configuration with Pydantic Settings
- [x] Set up Git repository and GitHub integration
- [x] Create comprehensive .gitignore for full-stack AI project

### Phase 2: Core AI Agent Development
- [ ] Implement basic Langchain agent
- [ ] Design conversation memory system
- [ ] Create personal preference learning mechanism
- [ ] Implement context-aware response generation
- [ ] Add conversation history storage
- [ ] Test basic conversational capabilities

### Phase 3: Task Management System
- [ ] Design task/todo data models
- [ ] Implement CRUD operations for tasks
- [ ] Create shopping list functionality
- [ ] Add task categorization and prioritization
- [ ] Implement task completion tracking
- [ ] Add natural language task creation

### Phase 4: Intelligent Reminder System
- [ ] Design reminder logic and triggers
- [ ] Implement time-based reminders
- [ ] Add context-aware reminder suggestions
- [ ] Create notification delivery system
- [ ] Implement reminder snoozing/rescheduling
- [ ] Add location-based reminders (future)

### Phase 5: Calendar Integration
- [ ] Research calendar API options (Google Calendar, Outlook)
- [ ] Implement calendar authentication
- [ ] Add event reading capabilities
- [ ] Implement event creation from natural language
- [ ] Add scheduling conflict detection
- [ ] Create meeting preparation reminders

### Phase 6: Web Interface Development
- [ ] Set up React/Next.js frontend
- [ ] Design UI/UX wireframes
- [ ] Implement chat interface
- [ ] Add task dashboard
- [ ] Create calendar view integration
- [ ] Add settings and preferences panel
- [ ] Implement responsive design

### Phase 7: API Integration & Testing
- [ ] Create comprehensive API endpoints
- [ ] Implement authentication system
- [ ] Add API rate limiting and security
- [ ] Write unit tests for core functions
- [ ] Implement integration tests
- [ ] Add end-to-end testing

### Phase 8: AWS Deployment
- [ ] Set up AWS account and IAM roles
- [ ] Create RDS PostgreSQL instance
- [ ] Set up EC2 instances for backend
- [ ] Configure S3 for static assets
- [ ] Set up CloudFront distribution
- [ ] Implement CI/CD pipeline
- [ ] Configure monitoring and logging
- [ ] Set up SSL certificates

### Phase 9: Advanced Features
- [ ] Add voice interaction capabilities
- [ ] Implement mobile responsiveness
- [ ] Add data export/import functionality
- [ ] Create backup and recovery system
- [ ] Add analytics and usage insights
- [ ] Implement multi-user support (future)

### Phase 10: MCP Migration (Future)
- [ ] Analyze current integrations for MCP compatibility
- [ ] Design MCP server architecture
- [ ] Implement MCP resources (calendar, tasks, preferences)
- [ ] Implement MCP tools (create_task, set_reminder, schedule_event)
- [ ] Create MCP security and permission framework
- [ ] Migrate Google Calendar integration to MCP resource
- [ ] Migrate task management to MCP tools
- [ ] Implement MCP client in AI agent
- [ ] Add third-party MCP server support
- [ ] Performance testing and optimization
- [ ] Documentation for MCP integrations

### Phase 11: Polish & Documentation
- [ ] Optimize performance
- [ ] Add comprehensive error handling
- [ ] Create user documentation
- [ ] Add developer documentation
- [ ] Implement feedback system
- [ ] Final testing and bug fixes

## 🚀 Getting Started

### Prerequisites
- Python 3.11.11 (managed via pyenv)
- Git
- OpenAI API key

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd agentic-first
   ```

2. **Set up Python environment:**
   ```bash
   pyenv local 3.11.11  # Ensure correct Python version
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env file with your OpenAI API key and other settings
   ```

5. **Run the application:**
   ```bash
   python -m app.main
   ```

6. **Access the application:**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

### Current Status
✅ **Backend Foundation**: FastAPI server with database models and configuration
🚧 **In Progress**: AI conversation engine and API routes  
📋 **Next**: Langchain integration and chat endpoints

## 📁 Project Structure

```
agentic-first/
├── README.md                    # Project documentation and progress tracking
├── .gitignore                   # Comprehensive ignore rules for full-stack AI project
├── .python-version              # Python version specification (3.11.11)
├── backend/                     # FastAPI backend application
│   ├── .env.example            # Environment variables template
│   ├── .env                    # Local environment variables (gitignored)
│   ├── requirements.txt        # Python dependencies
│   ├── venv/                   # Virtual environment (gitignored)
│   ├── logs/                   # Application logs (gitignored)
│   ├── credentials/            # API credentials (gitignored)
│   ├── chroma_db/              # Vector database storage (gitignored)
│   ├── tests/                  # Test files
│   └── app/
│       ├── __init__.py
│       ├── main.py             # FastAPI application entry point
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py       # Environment & settings management
│       │   └── database.py     # SQLAlchemy database setup
│       ├── models/
│       │   ├── __init__.py
│       │   ├── user.py         # User profile and preferences
│       │   ├── task.py         # Tasks, todos, shopping lists
│       │   └── conversation.py # Chat history and learned preferences
│       ├── api/                # API routes (in progress)
│       │   └── __init__.py
│       ├── services/           # Business logic services (planned)
│       ├── schemas/            # Pydantic schemas (planned)
│       └── utils/              # Utility functions (planned)
└── frontend/                   # Next.js frontend (planned)
    └── (to be created)
```

## 🔧 Configuration

### Environment Variables

The application uses environment variables for configuration. Copy `.env.example` to `.env` and configure:

```bash
# Core Settings
OPENAI_API_KEY=your_openai_api_key_here
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your_secret_key_here

# Database
DATABASE_URL=sqlite:///./ai_assistant.db

# AI Configuration  
AI_MODEL=gpt-4o-mini
AI_TEMPERATURE=0.7
AI_MAX_TOKENS=1000

# Google Calendar (for future integration)
GOOGLE_CREDENTIALS_PATH=credentials/google_credentials.json
GOOGLE_TOKEN_PATH=credentials/google_token.json

# ChromaDB (Vector Database)
CHROMA_PERSIST_DIRECTORY=./chroma_db
CHROMA_COLLECTION_NAME=ai_assistant_memory

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/ai_assistant.log

# Frontend CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

### Database Models

The application includes three main data models:

- **User**: Stores personal preferences, work habits, and settings
- **Task**: Manages todos, shopping lists, work deadlines, and reminders  
- **Conversation**: Maintains chat history and learned preferences for AI context

### Architecture Decisions

- **SQLite for Development**: Easy setup, file-based database
- **PostgreSQL for Production**: Scalable, robust database for deployment
- **Pydantic Settings**: Type-safe configuration management
- **SQLAlchemy ORM**: Database abstraction layer for flexibility

## 🤝 Contributing

*Guidelines for contributing to the project*

## 📄 License

*License information*

---

**Status**: 🚀 Building MVP - Phase 1 Complete, Phase 2 Starting
**Last Updated**: January 2025
**Next Milestone**: AI conversation engine with Langchain integration

## 🎯 MVP Focus
1. **Conversational AI** with OpenAI GPT-4 and memory persistence
2. **Task Management** for todos and shopping lists
3. **Google Calendar Integration** for event management
4. **Modern Web Interface** with Next.js, React, and Tailwind CSS
5. **Simple Reminder System** for key activities

## 🔄 MCP Migration Strategy

### **Why MCP Later?**
We're building with traditional Langchain first, then migrating to **Model Context Protocol (MCP)** for enhanced standardization and security.

#### **Current Approach (Phase 1)**
```python
# Direct integrations - fast development
calendar_service = build('calendar', 'v3', credentials=creds)
agent = create_langchain_agent(tools=[calendar_tool, task_tool])
```

#### **Future MCP Approach (Phase 10)**
```python
# Standardized protocol - enhanced security & composability
mcp_server = PersonalAssistantMCPServer()
mcp_server.register_resource("calendar://events")
mcp_server.register_tool("create_task")
```

### **MCP Benefits We'll Gain**
- 🔐 **Enhanced Security**: Fine-grained permissions per resource
- 🔧 **Tool Composability**: AI can chain multiple services automatically  
- 🌐 **Third-party Integration**: Open protocol for external developers
- 📊 **Standardized Interface**: Uniform way to access all services
- 🚀 **Scalability**: Better architecture for multiple AI clients

### **Migration Path**
1. **Build working MVP** with direct integrations
2. **Identify integration patterns** from real usage
3. **Design MCP resource/tool abstractions** 
4. **Gradual migration** service by service
5. **Enhanced features** possible only with MCP 