You are a Senior Software Architect with more than 10 years of experience in building AI SaaS applications.

Your task is to help design and guide the development of a complete software system based on the following project idea.

You must behave like a real software architect and produce a structured and professional output.

Do NOT give short answers. Provide detailed explanations, diagrams, architecture decisions, and implementation guidance.

Project Idea:

Students are required to submit a final year project report in a specific Word document format provided by their college. The report usually contains sections like cover page, certificate, acknowledgement, abstract, introduction, literature review, methodology, implementation, results, conclusion, and references.

Currently students manually copy content from AI tools like ChatGPT and then rewrite it using paraphrasing tools to avoid plagiarism. They also manually format the entire document according to strict formatting rules such as font, margins, spacing, page numbering, and section headings.

The idea is to build an AI-powered system that automatically generates a complete academic project report following the required formatting rules and allows the user to edit the document through a chat interface.

Main Features of the System:

1. AI-generated academic content for each report section.
2. User can define how many pages each section should contain.
3. The system must generate plagiarism-safe and human-like academic writing.
4. The system automatically formats the document according to college requirements (font, margin, spacing, headings).
5. The system shows a live preview of the generated document.
6. The user can modify the report using a chat interface.
7. The AI updates the document when the user requests changes.
8. The system exports the final document as DOCX and PDF.
9. Images or diagrams should not be generated; instead the system should leave blank placeholders for them.
10. The system should allow prompt templates for different report sections to improve content quality.

Example Interaction:

User input:
Project title: AI Based PDF Question Answering System
Introduction length: 1 page
Conclusion length: 2 pages
Technology stack: Python, LangChain, FAISS, Streamlit

The system should generate structured academic content for the report.

When the user types in chat:
"Add explanation of RAG architecture in methodology"

The AI should update the relevant section.

Constraints:

The project must be built with a budget of 0 dollars using open-source tools and free-tier services.

Possible technologies include:
Frontend: React or Streamlit
Backend: FastAPI or Flask
AI models: Open-source models or free APIs
Document generation: python-docx
Deployment: free hosting platforms

Now perform the following tasks step-by-step:

1. Write a complete Software Requirements Specification (SRS) document including:

   * Introduction
   * Purpose
   * Scope
   * Definitions
   * Overall description
   * Functional requirements
   * Non-functional requirements
   * System constraints
   * Use case diagrams
   * System architecture

2. Explain the complete system architecture including:

   * frontend architecture
   * backend architecture
   * AI generation pipeline
   * document generation pipeline
   * chat editing workflow

3. Design a clean project folder structure for the entire application.

4. Explain the main modules of the system such as:

   * AI content generation module
   * prompt template engine
   * chat modification system
   * document formatting engine
   * preview system
   * export system

5. Provide example prompts for each report section such as:

   * abstract
   * introduction
   * literature review
   * methodology
   * implementation
   * conclusion

6. Show example Python code snippets for:

   * generating DOCX files
   * integrating an LLM
   * implementing chat based document editing

7. Suggest how to deploy the system completely for free.

8. Suggest future improvements and advanced features that could make the project more impressive for academic evaluation.

Output must be structured with clear headings and professional explanation.
