#!/usr/bin/env bash

if [[ -n "${CIRCLE_PR_NUMBER}" ]]; then
  PR_INFO_URL=https://api.github.com/repos/$CIRCLE_PROJECT_USERNAME/$CIRCLE_PROJECT_REPONAME/pulls/$CIRCLE_PR_NUMBER
  PR_BASE_BRANCH=$(curl -L "$PR_INFO_URL" | python -c 'import json, sys; obj = json.load(sys.stdin); sys.stdout.write(obj["base"]["ref"])')
  git fetch origin +"$PR_BASE_BRANCH":circleci/pr-base
  # We need these config values or git complains when creating the
  # merge commit
  git config --global user.name "Circle CI"
  git config --global user.email "circleci@example.com"
  git merge --no-edit circleci/pr-base
fi
