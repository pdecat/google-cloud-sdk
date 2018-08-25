#!/bin/bash                                                                                                                                                   
set -e                                                                                                                                                        
                                                                                                                                                              
cd  /tmp/gcloud_history/                                                                                                                                      
git tag -l
git remote add origin https://${GH_TOKEN}@github.com/twistedpair/google-cloud-sdk.git > /dev/null 2>&1                                                        

git pull origin master --verbose

git push -u origin master --tags --verbose                                                                                                                              
git log --graph --oneline --decorate --all 
echo "git sync complete"                                                                                                                                      
