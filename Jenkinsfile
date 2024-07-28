pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'develop', url: 'https://github.com/Adarsh-Liju/json-validator'
            }
        }
        stage('Set up Environment') {
            steps {
                // Set up a virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment and install dependencies
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run Django tests
                sh '''
                    source venv/bin/activate
                    python manage.py test
                '''
            }
        }
        stage('Run Server') {
            steps {
                // Run Django development server
                sh '''
                    source venv/bin/activate
                    nohup python manage.py runserver 0.0.0.0:8000 &
                '''
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
        success {
            // Notify on success (optional)
            echo 'Build succeeded!'
        }
        failure {
            // Notify on failure (optional)
            echo 'Build failed!'
        }
    }
}
