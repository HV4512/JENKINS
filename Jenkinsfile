pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
      triggers{
<<<<<<< HEAD
        pollSCM '* * * * *'
=======
        pollSCM 'H/5 * * * *'
>>>>>>> 9821266b3bc1bbce2e890b70c57ffaeabf3f5b65
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
<<<<<<< HEAD
                cd myapp
                pip install -r requirements.txt
=======
                echo "doing build stuff.."
>>>>>>> 9821266b3bc1bbce2e890b70c57ffaeabf3f5b65
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
<<<<<<< HEAD
                cd myapp
                python3 hello.py
                python3 hello.py --name=Harsh
=======
                echo "doing test stuff.."
>>>>>>> 9821266b3bc1bbce2e890b70c57ffaeabf3f5b65
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}