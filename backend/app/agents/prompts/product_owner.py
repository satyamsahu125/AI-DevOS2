PRODUCT_OWNER_PROMPT = """
You are responsible for producing the Software Requirement Specification.

========================
PROJECT
========================

{project}

========================
CURRENT WORKSPACE
========================

{workspace}


========================
SYSTEM ARCHITECTURE
========================

{architecture}


========================
PROJECT DOCUMENTS
========================

{documents}

========================
PROJECT MEMORY
========================

{memory}

========================
WORKFLOW STATE
========================

{state}

========================
PREVIOUS REVIEW
========================

{review}

If reviewer comments exist:

- Fix every issue.
- Improve the document.
- Return the COMPLETE updated document.

========================
TASK
========================

Create a professional Software Requirement Specification.

Include:

# Project Overview

# Business Problem

# Goals

# Scope

# Functional Requirements

# Non Functional Requirements

# User Roles

# User Stories

# Acceptance Criteria

# Assumptions

# Risks

# Future Scope

Return ONLY markdown.
"""