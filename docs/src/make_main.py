import os
import shutil
import tempfile
import git
import glob
from sphinx.cmd import build

if __name__ == '__main__':

    BUILD_DIR = tempfile.mkdtemp()
    BUILD_HTML_DIR = os.path.join(BUILD_DIR, "html")
    BUILD_PDF_DIR = os.path.join(BUILD_DIR, "pdf")
    SOURCE_DIR = os.getcwd()
    TARGET_DIR = os.path.join(SOURCE_DIR, "out")
    TARGET_HTML_DIR = os.path.join(TARGET_DIR, "html")
    TARGET_PDF_DIR = os.path.join(TARGET_DIR, "pdf")

    x = build.main([
        '-b',
        'html',
        SOURCE_DIR,
        BUILD_HTML_DIR,
    ])
    if not x:
        shutil.rmtree(TARGET_HTML_DIR, ignore_errors=True)
        shutil.move(BUILD_HTML_DIR, TARGET_HTML_DIR)
        if os.path.isfile(os.path.join(TARGET_HTML_DIR, ".buildinfo")):
            os.remove(os.path.join(TARGET_HTML_DIR, ".buildinfo"))
        shutil.rmtree(os.path.join(TARGET_HTML_DIR, ".doctrees"))
        shutil.rmtree(os.path.join(TARGET_HTML_DIR, "_sources"))

    x = build.main([
        '-M',
        'latexpdf',
        SOURCE_DIR,
        BUILD_PDF_DIR,
    ])
    if not x:
        shutil.rmtree(TARGET_PDF_DIR, ignore_errors=True)
        os.mkdir(TARGET_PDF_DIR)
        os.rename(
            os.path.join(BUILD_PDF_DIR, "latex", "ewan-isp.pdf"),
            os.path.join(TARGET_PDF_DIR, "ewan-isp.pdf"),
        )

    git_repo = False
    trav = os.getcwd()
    while trav != '/':
        if os.path.exists(os.path.join(trav, '.git')):
            git_repo = trav
            break
        trav = os.path.dirname(trav)

    if git_repo:
        repo = git.Repo(git_repo)

        files = [fname for fname in glob.iglob(
            os.path.join(TARGET_DIR, "**/*"), recursive=True)]
        xgit = repo.git
        xgit.add(files + [SOURCE_DIR])
        git_msg = u"[DOCS]][{}] HTML and PDF generated files".format(
            "addons_isp")
        xgit.commit('-m', git_msg, files)
        commit = repo.head.commit
        branch = repo.head.ref.name
        hexsha = commit.hexsha
        xgit.push('origin', '{}:{}'.format(hexsha, branch))
