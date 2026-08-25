# AI Talent Mapper

### Find Right Talent. For Right Role. For Right Impact.

AI Talent Mapper is a bilingual talent and behavioral-pattern assessment prototype developed by **Vidhishastra Foundation**.

It evaluates 21 assessment responses, identifies natural talent patterns, suggests career paths, calculates role compatibility and generates a professional PDF report.

> This prototype is intended for talent exploration. It is not a clinical or psychological diagnosis.

## Live Project

- **Public Demo:** https://ai-talent-mapper.onrender.com/demo
- **API Documentation:** https://ai-talent-mapper.onrender.com/docs
- **Health Check:** https://ai-talent-mapper.onrender.com/health
- **GitHub Repository:** https://github.com/prithabi/ai-talent-mapper

> The free Render instance may take approximately 50 seconds to wake up after inactivity.

## Current Features

- Mobile-responsive public assessment page
- 21 bilingual questions in Hindi and English
- Rating scale from 1 to 5
- Candidate-name input
- Six Intelligence/Talent Codes
- Primary and secondary talent-code identification
- Talent profile and strengths generation
- Suggested career paths
- Role Compatibility Index (RCI)
- Team-synergy analysis
- One-click assessment and PDF generation
- Professional downloadable PDF report
- Interactive Swagger API documentation
- Public health-check endpoint
- Secure public question delivery without exposing scoring codes

## Intelligence Code Framework

The current prototype includes six Intelligence Codes:

- **EI2** — Explorer Intelligence
- **9HY** — Agile/Kinetic Intelligence
- **80L** — Visual-Spatial Intelligence
- **O21** — Social-Linguistic Intelligence
- **23BR** — Logical-Analytical Intelligence
- **D1** — Self-Reliant/Action Intelligence

## Assessment Workflow

1. Candidate enters their name.
2. Candidate answers 21 bilingual questions.
3. The scoring engine processes ratings from 1 to 5.
4. Primary and secondary talent codes are identified.
5. Talent profile, strengths and career paths are generated.
6. Role-compatibility scores are calculated.
7. A professional PDF report is downloaded.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Service health check |
| GET | `/demo` | Public assessment interface |
| GET | `/questions` | Public bilingual questions |
| POST | `/assess` | Assess candidate responses |
| POST | `/team-synergy` | Calculate team synergy |
| POST | `/candidate-report` | Generate PDF from result data |
| POST | `/assess-and-report` | Assess candidate and generate PDF |

## Technology Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- ReportLab
- HTML, CSS and JavaScript
- JSON-based assessment data
- GitHub
- Render

## Project Structure

```text
ai-talent-mapper/
├── api/
│   └── main.py
├── data/
│   └── questions.json
├── demo/
│   └── index.html
├── models/
├── reporting/
│   └── pdf_report.py
├── scoring/
│   ├── scoring_engine.py
│   ├── role_compatibility.py
│   └── team_synergy.py
├── utils/
├── requirements.txt
└── README.md
```

## Verified Prototype Status

- [x] API deployed successfully
- [x] Public mobile demo live
- [x] 21 bilingual questions loaded
- [x] Assessment scoring working
- [x] Talent profiles generated
- [x] Role Compatibility Index working
- [x] Team-synergy endpoint working
- [x] Professional PDF report working
- [x] Complete end-to-end mobile test passed
- [x] HTTP 200 health verification passed

## Future Development

- Secure candidate and administrator accounts
- HR dashboard and candidate management
- Assessment history and database storage
- Team-synergy heatmap interface
- Additional talent and role frameworks
- Multilingual expansion
- Bias and fairness evaluation
- Data privacy and security controls
- Automated testing and monitoring
- Custom organizational assessment models

## Purpose

The purpose is not simply to measure marks or degrees. The purpose is to understand:

> What kind of intelligence does a person naturally possess, and where can that intelligence create the greatest positive impact?

## Organization

Developed by **Vidhishastra Foundation**

© 2026 Vidhishastra Foundation
