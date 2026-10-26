pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                echo 'Fetching source code from GitHub repository...'
                git branch: 'main', url: 'https://github.com/BALERION18/devops_ass2.git'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Executing automated tests to verify the presence of the form and required input fields...'
                script {
                    if (isUnix()) {
                        sh 'python3 test_form.py || python test_form.py'
                    } else {
                        bat 'python test_form.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully: Form and all required input fields verified.'
        }
        failure {
            echo 'Pipeline failed: HTML form verification tests failed.'
        }
    }
}
