from pathlib import Path

import markdown
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
)


class ReportService:

    ############################################################

    @staticmethod
    def _slug(name: str) -> str:

        return (
            name.lower()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("?", "")
            .replace(":", "")
            .replace(".", "")
        )

    ############################################################

    @classmethod
    def save_markdown(
        cls,
        report: str,
        run_directory: Path,
        filename: str,
    ) -> Path:

        filepath = (
            run_directory
            / f"{cls._slug(filename)}.md"
        )

        filepath.write_text(
            report,
            encoding="utf-8",
        )

        print(f"✓ Saved {filepath.name}")

        return filepath

    ############################################################

    @classmethod
    def save_html(
        cls,
        report: str,
        run_directory: Path,
        filename: str,
    ) -> Path:

        body = markdown.markdown(
            report,
            extensions=[
                "tables",
                "fenced_code",
            ],
        )

        html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<title>{filename}</title>

<style>

body {{
font-family: Arial;
max-width:1100px;
margin:auto;
padding:50px;
line-height:1.8;
background:#fafafa;
}}

h1 {{
color:#2563eb;
}}

h2 {{
margin-top:35px;
color:#1d4ed8;
}}

table {{
border-collapse:collapse;
width:100%;
}}

table,th,td {{
border:1px solid #ddd;
}}

th,td {{
padding:10px;
}}

pre {{
background:#f4f4f4;
padding:15px;
}}

code {{
background:#eee;
padding:2px 5px;
}}

</style>

</head>

<body>

{body}

</body>

</html>
"""

        filepath = (
            run_directory
            / f"{cls._slug(filename)}.html"
        )

        filepath.write_text(
            html,
            encoding="utf-8",
        )

        print(f"✓ Saved {filepath.name}")

        return filepath

    ############################################################

    @classmethod
    def save_pdf(
        cls,
        report: str,
        run_directory: Path,
        filename: str,
    ) -> Path:

        filepath = (
            run_directory
            / f"{cls._slug(filename)}.pdf"
        )

        document = SimpleDocTemplate(
            str(filepath)
        )

        styles = getSampleStyleSheet()

        story = []

        for line in report.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(
                        line,
                        styles["BodyText"],
                    )
                )

        document.build(story)

        print(f"✓ Saved {filepath.name}")

        return filepath