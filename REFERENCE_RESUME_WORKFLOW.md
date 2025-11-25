# Reference Resume Library Workflow

## Overview

You'll maintain a library of reference resumes for different roles. The skill will:
1. Analyze the job description
2. Find the best matching reference resume
3. Use that as the base to create a tailored .md file
4. The populate script will use ONLY the .md content (ignoring template content)

---

## Setup Your Reference Resume Library

### Folder Structure
```
resumes/
├── refrence_resume/           ← Your reference library
│   ├── Data Engineer.md
│   ├── Data Analyst.md
│   ├── Data Lead.md
│   ├── AI Engineer.md
│   ├── Business Intelligence Lead.md
│   └── ... (more variations)
├── Template/
│   └── Template.docx
└── [generated resumes will go here]
```

### Naming Convention for Reference Resumes

Use clear, descriptive names that indicate the role type:
- `Data Engineer.md`
- `Senior Data Analyst.md`
- `Data Lead.md`
- `AI ML Engineer.md`
- `Business Intelligence Lead.md`
- `Analytics Manager.md`

The skill will match based on:
- Job title keywords
- Required skills
- Seniority level
- Domain focus

---

## How the Skill Will Match

### Matching Logic:

1. **Parse job description** to extract:
   - Job title
   - Key skills/technologies
   - Seniority level (Senior, Lead, Manager, etc.)
   - Domain (Data Engineering, Analytics, AI/ML, etc.)

2. **Scan reference_resume folder** for all .md files

3. **Score each reference resume** based on:
   - Filename match with job title keywords (40%)
   - Content match with job requirements (30%)
   - Seniority level match (20%)
   - Domain/specialization match (10%)

4. **Select best match** and announce to user:
   ```
   Based on the job description analysis:
   - Job Title: "Senior Data Engineer"
   - Key Skills: Python, Airflow, GCP, SQL
   - Domain: Data Engineering

   Selected reference resume: "Data Engineer.md" (95% match)

   This resume will be used as the base for tailoring.
   ```

5. **Build tailored resume** using:
   - Content from selected reference resume
   - Reframed to match job requirements
   - Additional emphasis on matching skills
   - Same structure as reference resume

---

## What Goes in Reference Resumes

Each reference resume should be in the **NEW FORMAT** (matching the template):

```markdown
# ISHUPAL SINGH
## DATA ENGINEER

email | phone | location | LinkedIn

---

## CAREER PROFILE

{First-person paragraph emphasizing DATA ENGINEERING experience, cloud platforms, ETL pipelines, etc.}

---

## AREAS OF EXPERTISE

**Data Engineering & ETL:** {Focus on pipeline building, data architecture}
**Cloud Platforms & Big Data:** {Focus on GCP, Spark, etc.}
**Programming & Automation:** {Focus on Python, SQL, etc.}

---

## CAREER SUMMARY

{List all jobs}

---

## Work Experience

{Emphasize data engineering responsibilities and achievements}

---

## Education
## Skills
## References
```

### Key Points:

1. **Each reference resume** is a complete, standalone resume
2. **Emphasize different aspects** of your experience based on the target role
3. **Use the NEW template format** (paragraphs for responsibilities, bullets for achievements)
4. **Career Profile** should be written for that specific role type

---

## Example: Creating Reference Resumes

### Data Engineer.md
- Career Profile: Emphasize pipeline building, ETL, data architecture
- Areas of Expertise: Data Engineering, Cloud Platforms, Big Data
- Work Experience: Highlight technical implementation work
- Skills: Python, Airflow, Spark, GCP, Kafka, etc.

### Data Analyst.md
- Career Profile: Emphasize insights, visualization, stakeholder communication
- Areas of Expertise: Analytics, BI Tools, Data Storytelling
- Work Experience: Highlight analysis, reporting, dashboard work
- Skills: SQL, Tableau, Python, Excel, Power BI, etc.

### Data Lead.md
- Career Profile: Emphasize team leadership, strategic vision, delivery
- Areas of Expertise: Team Leadership, Strategic Planning, Stakeholder Management
- Work Experience: Highlight people management, governance, cross-functional work
- Skills: Leadership, Agile, Governance, plus technical skills

### AI Engineer.md
- Career Profile: Emphasize ML models, AI implementation, GenAI
- Areas of Expertise: Machine Learning, AI/GenAI, Model Development
- Work Experience: Highlight AI/ML projects, model building, deployment
- Skills: Python, TensorFlow, LLMs, RAG, NLP, etc.

---

## Updated Workflow

### Step 1: You Ask Me to Use the Skill
```
"Use the resume-tailoring skill for this job: [paste job description]"
```

### Step 2: Skill Analyzes and Selects Reference Resume
```
I analyze the JD and say:
"Analyzing job description...
Role: Senior Data Engineer
Key requirements: Python, Airflow, GCP, BigQuery, ETL

Scanning reference resume library...
Found 5 reference resumes

Best match: 'Data Engineer.md' (92% match)
- Strong alignment with pipeline/ETL focus
- Matches cloud platform requirements
- Appropriate seniority level

Using this as base for tailoring..."
```

### Step 3: Skill Generates Tailored .md File
```
The skill:
1. Loads "Data Engineer.md" as the base
2. Analyzes what content from your reference resume matches the JD
3. Reframes/emphasizes relevant parts
4. Generates: "Ishupal Singh - [Company] [Role] Resume.md"
```

### Step 4: You Run the Population Script
```bash
python populate_new_template.py
```

The script:
- Finds the newly generated .md file
- Uses ONLY content from that .md file
- Populates the template with that content
- Saves: "[Company] [Role] - NEW TEMPLATE.docx"

---

## Key Changes Needed

### 1. Update Resume-Tailoring Skill
Add this logic to the skill:

```markdown
## Phase 0.5: Reference Resume Selection (NEW)

**Before building from library, select best reference resume:**

1. **Scan reference_resume folder:**
   ```
   Use Glob tool: pattern="*.md" path="resumes/refrence_resume/"
   ```

2. **For each reference resume:**
   - Read filename
   - Read content (first 500 lines to get overview)
   - Extract: title, skills, experience areas

3. **Score against job description:**
   - Filename keyword match: 40%
   - Content skill match: 30%
   - Seniority level: 20%
   - Domain alignment: 10%

4. **Select best match and inform user:**
   ```
   "Selected reference resume: '{filename}' ({score}% match)
   Rationale: {why this resume matches the job}"
   ```

5. **Use selected resume as base:**
   - All content comes from this reference resume
   - Tailor/reframe based on job requirements
   - Maintain structure and format
```

### 2. Update populate_new_template.py

**Current issue:** The script tries to map .md content to template positions

**New approach:** Use .md content to COMPLETELY REPLACE template content

```python
# Instead of mapping to specific line numbers,
# generate the DOCX from scratch using the .md structure
# Or: Clear template and rebuild from .md only
```

---

## Benefits of This Approach

1. **Consistency:** Each role type has optimized framing
2. **Speed:** Start with proven base instead of building from scratch
3. **Quality:** Reference resumes are pre-refined and tested
4. **Flexibility:** Easy to add new role variations
5. **Control:** You maintain the reference library

---

## Next Steps

1. **Create your reference resumes:**
   - Start with 3-4 main role types
   - Use the NEW template format
   - Emphasize different aspects of your experience

2. **I'll update the skill:**
   - Add reference resume selection logic
   - Make it choose the best match
   - Use that as the base

3. **I'll update populate_new_template.py:**
   - Make it use ONLY .md content
   - Ignore template pre-filled content
   - Generate fresh DOCX from .md

---

## Example Reference Resume Names

Based on your background, suggested reference resumes:

1. `Data Engineer - Cloud Platforms.md` (for pipeline/ETL roles)
2. `Data Lead - Analytics.md` (for leadership roles)
3. `AI ML Engineer.md` (for ML/AI focused roles)
4. `Data Analyst - BI.md` (for analyst roles)
5. `Insights Lead - Governance.md` (for governance/compliance focus)

Each optimized for different job types you might apply to.

---

## Summary

**Old workflow:** Skill builds from generic library → populates template

**New workflow:** Skill finds best reference resume → tailors it → populates template with ONLY .md content

This gives you much more control and consistency!
