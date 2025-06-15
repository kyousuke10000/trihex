# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TriHexφ is a comprehensive soul diagnosis and self-understanding system with 216 soul types based on a 3-dimensional classification:
- **先天 (Innate - 6 Spirals)**: 地・水・火・風・空・識 (elemental/destiny aspects)
- **後天 (Acquired - 6 Systems)**: 智略・共鳴・行動・創造・直感・信念 (values/experience)
- **顕現 (Manifestation - 6 Wisdoms)**: 數理・陰陽・易変・螺律・霊脈・真形 (ideals/future)

## Architecture

### Core Components
- `src/trihex-core/`: Documentation, philosophy, and system specifications
- `src/trihex_gpt_custom/`: Streamlit web app for soul diagnosis
- `src/soul-diagnosis-webhook/`: Flask API for Google Sheets integration
- `src/trihex-infra/`: Cloudflare Workers for API proxying
- `src/truthsphere-engine/`: Quartz dialogue model implementation
- `docs/`: Project documentation
- `assets/`: Static assets and resources
- `data/`: Data files and configurations

### Two Main GPT Systems
1. **Truthsphere GPT (スフィ)**: Deep dialogue using Quartz Model (6-stage process)
2. **TriHexφ Diagnostic GPT**: Initial public diagnosis tool

## Common Commands

### Python Applications

#### Streamlit App (src/trihex_gpt_custom/)
```bash
cd src/trihex_gpt_custom/
pip install -r requirements.txt
streamlit run app.py
```

#### Flask Webhook (src/soul-diagnosis-webhook/)
```bash
cd src/soul-diagnosis-webhook/
pip install -r requirements.txt
python app.py
```

### Cloudflare Workers

#### Deploy Cloudflare Worker
```bash
cd src/trihex-infra/cloudflare/flask_proxy/
wrangler deploy
```

### Testing

#### Run Tests
```bash
pip install pytest
pytest tests/
```

## Key Data Files

- `src/trihex-core/docs/07_data/soulbook_master_v1.json`: Master soul type definitions
- `src/trihex_gpt_custom/data/eto_classification_dict.json`: Zodiac classification data
- `src/trihex_gpt_custom/templates/`: Various template files for soul diagnosis output

## Development Guidelines

### File Naming Conventions
Follow `src/trihex-core/docs/05_guidelines/naming_convention.md` for consistent naming patterns.

### Writing Style
Adhere to `src/trihex-core/docs/05_guidelines/writing_style_guide.md` for documentation and user-facing content.

### PDF Generation
The system uses `weasyprint` for PDF generation of soul diagnosis results. Templates are in HTML format with Japanese font support (Noto Sans JP).

## Integration Points

- Google Sheets integration via `gspread` and OAuth2
- Slack notifications via webhook
- Cloudflare Workers for API proxying and security
- Astrology calculations using `pyswisseph` and `ephem`

## Security Notes

- API keys and credentials should use environment variables
- Cloudflare Workers act as proxy layer for external API access
- OAuth2 service account credentials required for Google Sheets access