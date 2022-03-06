pipeline {
    agent any
    stages {
        stage('Clean Jenkins Workspace') {
            steps {
                cleanWs()
            }
        }
        
        stage('Check Vars') {
            steps {
                sh "echo check first if vars are compliant"
                sh "echo ENV: $ENV"
                sh "echo GIT_BRANCH: $GIT_BRANCH"
                sh "echo RELEASE_VERSION: $VERSION"
            }
        }
        
        stage('Checkout git') {
            steps {
                git(
                    url: 'https://github.com/lcshlr/toxicity_monitor.git',
                    branch: "${GIT_BRANCH}"
                )
                sh "pwd"
                sh "ls"
            }
        }
        stage('Build docker and run'){
            steps {
                sh 'docker-compose up -d'
            }
        }
        
        stage('Testing + upload release '){
            steps {
                dir('public') {
                    sh 'cypress run'
                }
                withCredentials([gitUsernamePassword(credentialsId: '507ac7f7-f087-4b36-a905-b099930ee564',
                 gitToolName: 'git-tool')]) {
                     sh "git checkout -b release-${VERSION}"
                     sh "git push -u origin release-${VERSION}"
                 }
            }
        }
    }
}
