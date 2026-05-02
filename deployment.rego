
package cicd.deploy

default allow = false

allow {
  input.image.signed == true
  count(input.vulnerabilities.critical) == 0
  input.build.source == "github-actions"
}
