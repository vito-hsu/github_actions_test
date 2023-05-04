# Step1. PULL files from GitHub
#   git init
#   git remote add origin https://github.com/vito-hsu/github_actions_test.git
#   git pull origin main

# Step2. PUSH (updated) files to GitHub
#   git add .
#   git commit -m 'first version'
#   git push origin main


def test_1():
    a = 1 + 1
    b = 2 + 2
    assert b > a


def test_2():
    a = 2 + 2
    b = 4 + 4
    assert a < b


def test_3():
    a = 2 + 2
    b = 4 + 4
    assert a == b