node {
  stage('SCM') {
    git branch: 'main',
    url: 'https://github.com/surajchauhan-k/demo.git'
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}