# Updated Markdown Generation Format for SKILL.md

## REPLACE the "4.1 Markdown Generation" section (lines 688-744) with this:

**4.1 Markdown Generation:**

**Compile mapped content into clean markdown that matches the template structure:**

```markdown
# {FULL_NAME}
## {Job_Title}

{Email} | {Phone} | {Location} | {LinkedIn_URL}

---

## CAREER PROFILE

{Write a single comprehensive paragraph (5-7 sentences) in FIRST PERSON ("I") voice that includes:
- Years of experience and core expertise areas
- Specialized focus (e.g., "I specialize in AI powered solutions...")
- Balance between strategic vision and hands-on execution
- Technical strengths and approach
- Personal motivation ("What drives me is...")

Style: Personal, conversational but professional, showing personality}

---

## AREAS OF EXPERTISE

**{Expertise_Area_1_Title}:** {Detailed paragraph describing this expertise area, including specific technologies, approaches, and outcomes. Should be 2-3 sentences explaining depth of capability.}

**{Expertise_Area_2_Title}:** {Detailed paragraph for second area of expertise with similar depth and specificity.}

**{Expertise_Area_3_Title}:** {Detailed paragraph for third area of expertise.}

---

## CAREER SUMMARY

{Job_Title_1}, {Department/Team}, {Company}                                    {Dates}
{Job_Title_2}, {Department/Team}, {Company}                                    {Dates}
{Job_Title_3}, {Department/Team}, {Company}                                    {Dates}
{... list ALL roles, even brief/older ones}

---

## Work Experience

### {Job_Title_1}, {Department/Team}                                           {Dates}
**{Company} | {Location}**

{Paragraph 1: Opening overview of role, team size, and primary responsibilities. Full sentences describing what you led/managed/delivered.}

{Paragraph 2: Additional key responsibilities. Describe partnerships, stakeholder engagement, technical work. Full paragraphs, NOT bullets.}

{Paragraph 3: More responsibilities if role warrants it. Continue with full sentences describing scope and impact.}

{Paragraph 4: Additional responsibilities for major roles only.}

**Achievements**
- {Achievement 1 with specific metrics and quantified impact}
- {Achievement 2 with specific metrics and quantified impact}
- {Achievement 3 with specific metrics and quantified impact}
- {Achievement 4 with specific metrics and quantified impact - for major roles}

---

### {Job_Title_2}, {Department/Team}                                           {Dates}
**{Company} | {Location}**

{Paragraph 1: Overview and key responsibilities for this role}

{Paragraph 2: Additional responsibilities if warranted}

**Achievements**
- {Achievement 1 with metrics}
- {Achievement 2 with metrics}
- {Achievement 3 with metrics}

---

### {Job_Title_3 (if older/shorter role)}                                      {Dates}
**{Company} | {Location}**

{Single paragraph summarizing the role and key contributions. No separate Achievements section for very old roles.}

---

{Repeat pattern for all roles}

---

## Education

**{University_Name}**  -   {Date_Range}
{Degree_Name} {Specialization/Major}

**{University_Name_2}**  -   {Date_Range}
{Degree_Name} {Specialization/Major}

---

## Skills

**{Category_1_Name}**
{Skill1}, {Skill2}, {Skill3}, {Skill4}, {Skill5}, etc.

**{Category_2_Name}**
{Skill1}, {Skill2}, {Skill3}, {Skill4}, etc.

**{Category_3_Name}**
{Skill1}, {Skill2}, {Skill3}, etc.

{Repeat for 5-6 skill categories}

---

## References

Available on request
```

---

## KEY FORMATTING RULES

### Career Profile:
- **MUST** be written in first person ("I", "my", "me")
- **MUST** be a single large paragraph (5-7 sentences)
- **MUST** show personality and motivation
- **MUST** be conversational but professional
- Include a sentence starting with "What drives me is..." or "What excites me is..."

### Areas of Expertise:
- **Exactly 3 areas**
- Each with **bold title** followed by **detailed paragraph** (not bullets)
- Paragraphs should be 2-3 sentences
- Include specific technologies and outcomes

### Career Summary:
- **List ALL jobs** (even short/old ones)
- Format: `Title, Department, Company` followed by lots of spacing, then `Dates`
- **NO descriptions** - just title and dates

### Work Experience:

#### For Recent/Major Roles (2-3 most recent):
- Title and dates on same line (use lots of spacing)
- Company | Location on next line
- **3-4 paragraphs** describing responsibilities (NOT bullets)
- Paragraphs are full sentences describing what you did
- Separate "**Achievements**" section with **4-5 bullet points**
- Each achievement MUST include specific metrics/numbers

#### For Mid-Level Roles (next 2-3 roles):
- Same title/company format
- **1-2 paragraphs** for responsibilities
- "**Achievements**" section with **2-3 bullets**
- Still include metrics

#### For Older/Brief Roles (remaining roles):
- Same title/company format
- **Single paragraph** only
- **NO** separate Achievements section
- Summarize key contributions in paragraph

### Skills:
- **Grouped by category** (5-6 categories typical)
- Category name in **bold**
- Skills listed as **comma-separated** items (NOT bullets)
- Categories should cover: Technical, Tools/Platforms, Methodologies, Domain expertise

### Education:
- Format: `University  -   Date range` (note the spacing)
- Next line: Degree name and specialization
- NO "Bachelor of" or "Master of" prefix - just degree type and field

---

## IMPORTANT: PARAGRAPHS vs BULLETS

**Responsibilities = PARAGRAPHS** (full sentences, storytelling)
**Achievements = BULLETS** (with metrics)

Example of correct format:

```markdown
### Data and AI Insights Lead, Customer Complaints                            Dec 2023 - Present
**ANZ | Melbourne, Australia**

Lead team of 11 data professionals delivering enterprise analytics and regulatory reporting, establishing best-practice governance for Tableau visualization standards across retail operations.

Partner with executive, compliance, and technical stakeholders to translate regulatory requirements into delivery roadmaps. Use advanced SQL and data modeling concepts to transform raw compliance data into strategic business opportunities.

**Achievements**
- Built CRAIG, ANZ's first production generative AI tool, reducing manual complaint analysis time by 80% using Claude API and SBERT models with ChromaDB
- Architected end-to-end cloud analytics platform integrating Salesforce data through GCP BigQuery, processing 1M+ records daily
- Automated 6-monthly ASIC complaints data submission, eliminating 100% of manual compilation effort
```

---

## TONE AND VOICE

**Career Profile only:**
- Use first person ("I", "my", "me")
- Be conversational and show personality
- Example: "What drives me is identifying where emerging technologies can solve business problems in ways that weren't possible before"

**Rest of resume:**
- Use third person implied (no "I" but no "he/she" either)
- Example: "Lead team of 11..." not "I lead team of 11..."
- Active voice, strong action verbs
- Professional but not stiff

---

## METRICS AND QUANTIFICATION

**EVERY achievement bullet MUST include:**
- Specific numbers (percentages, counts, time savings, etc.)
- Clear before/after or impact statement
- Technologies/tools used when relevant

Bad: "Improved team performance"
Good: "Accelerated team delivery velocity by 35% through implementing Agile practices"

Bad: "Built an AI tool"
Good: "Built CRAIG, reducing manual analysis time by 80% (from hours to minutes) using Claude API and SBERT models"

---

## SECTION ORDERING (REQUIRED)

1. Header (Name, Title, Contact)
2. Career Profile
3. Areas of Expertise
4. Career Summary
5. Work Experience
6. Education
7. Skills
8. References

Do NOT change this order.
