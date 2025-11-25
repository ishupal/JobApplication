"""
Resume Generator Web App
Simple Flask app to generate resumes from mobile/browser
"""
from flask import Flask, render_template, request, send_file, jsonify
import os
import sys
from datetime import datetime

# Add parent directory to path to import your existing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'generated_resumes')

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    """Main page with job description form"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_resume():
    """Generate resume from job description"""
    try:
        # Get form data
        job_title = request.form.get('job_title', '')
        company = request.form.get('company', '')
        job_description = request.form.get('job_description', '')

        if not job_description:
            return jsonify({'error': 'Job description is required'}), 400

        # TODO: Here you would call your resume generation logic
        # For now, this is a placeholder that shows the structure

        # Step 1: Check for reference resumes
        # reference_resumes = check_reference_resumes()

        # Step 2: Generate .md file using resume-tailoring skill
        # This would call Claude API with your prompt
        # md_file = generate_markdown_resume(job_title, company, job_description)

        # Step 3: Convert .md to DOCX using your existing script
        # docx_file = convert_md_to_docx(md_file)

        # For now, return success message
        result = {
            'status': 'success',
            'message': f'Resume generation initiated for {job_title} at {company}',
            'timestamp': datetime.now().isoformat()
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download/<filename>')
def download_file(filename):
    """Download generated resume"""
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename
            )
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/status')
def status():
    """Check if service is running"""
    return jsonify({
        'status': 'running',
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)
