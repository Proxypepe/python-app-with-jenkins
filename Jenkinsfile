def imageName = 'proxypepe/demo'
def registry = 'http://localhost:5000'

def commitID() {
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    commitID
}

node('master'){
  stage('Checkout') {
    checkout scm
  }
    // stage('Unit Tests'){
  //   def imageTest = docker.build("${imageName}-test", 
  //   "-f Dockerfile.test .")
  //   imageTest.inside{
  //     sh 'python test_main.py'
  //   }
  //   // sh "docker run --rm -v $PWD/reports:/app/reports ${imageName}-test"
  //   // junit "$PWD/reports/*.xml"
  // }
  def imageTest = docker.build("${imageName}-test", "-f Dockerfile.test .")
  stage('Pre-integration Tests'){
    parallel(
      'Quality Tests': {
          sh "docker run --rm ${imageName}-test pylint ."
      },
       'Unit Tests': {
          sh "docker run --rm ${imageName}-test pytest"
        },
      'Security Tests': {
        sh "docker run --rm ${imageName}-test safety check -r main.py"
      }
    )
  }

  stage('Build') {
    docker.build("${imageName}", "-f Dockerfile .")
  }


  stage ('Image security test') {
    sh "docker run "
  }

  stage('Push') {
    docker.withRegistry(registry) {
      // docker.image(imageName).push(env.BUILD_ID)
      docker.image(imageName).push(commitID())

      if (env.BRANCH_NAME == 'main') {
          docker.image(imageName).push('main')
      }
    }
  }
}
