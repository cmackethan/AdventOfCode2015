import os

cwd = os.getcwd()
ls = os.listdir(cwd)
ls.remove('.git')

for fname in ls:
    fpath = os.path.join(cwd, fname)
    if os.path.isdir(fpath):
        print(fpath + '/input.txt')
        os.system('git rm --cached ' + fpath + '/input.txt')
        os.system('git rm --cached ' + fpath + '/testinput.txt')
        os.system('git rm --cached ' + fpath + '/output.txt')