# Resume Generator with Claude Code

Automated resume generation workflow using Claude Code's resume-tailoring skill and Python scripts.

## Features

- **Reference Resume Library:** Maintain multiple resume variations (Data Engineer, Data Lead, etc.)
- **Intelligent Matching:** Automatically selects the best reference resume for each job
- **Resume Tailoring Skill:** Uses Claude Code's skill to generate tailored markdown resumes
- **Template Population:** Converts markdown to professionally formatted DOCX files

## Project Structure

```
JobApplication/
├── .claude/
│   └── skills/
│       └── resume-tailoring/    # Claude Code skill (self-contained)
├── resumes/
│   ├── refrence_resume/         # Your reference resume library (.md files)
│   └── Template/                # DOCX template
├── web_app/                     # Flask web app for md → docx conversion
├── populate_new_template.py     # Main script to populate template
└── *.md                         # Documentation files
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Reference Resumes

Create your reference resumes in `resumes/refrence_resume/`:
- `Data Engineer.md`
- `Data Analyst.md`
- `Data Lead.md`
- etc.

Each should be a complete resume in markdown format.

### 3. Configure Template

Your DOCX template should be in `resumes/Template/Template.docx`

## Usage

### Local Usage

1. **Generate Resume using Claude Code:**
   ```
   Ask Claude: "Use the resume-tailoring skill for [job description]"
   ```

2. **Convert to DOCX:**
   ```bash
   python populate_new_template.py
   ```

### Claude Code Web Usage

1. Open [claude.ai/code](https://claude.ai/code) on any device
2. Navigate to this project folder
3. Ask Claude to use the resume-tailoring skill
4. Download the generated .md file
5. (Optional) Use the web converter to get DOCX

## Documentation

- `REFERENCE_RESUME_WORKFLOW.md` - How reference resumes work
- `RESUME_MARKDOWN_FORMAT_INSTRUCTIONS.md` - .md format specifications
- `HOW_TO_USE.md` - Usage guide

## Requirements

- Python 3.8+
- python-docx
- Claude Code (for resume generation)

## Notes

- Personal resumes (.md, .docx) are gitignored for privacy
- Reference resumes in `resumes/refrence_resume/` can be committed
- Template files are included in repository
