import subprocess
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

folder_in = "/home/user/tst"
folder_out = "/home/user/out"

def test_step1():
    # test1
    res1 = checkout(f'cd {folder_in}; 7z l {folder_out}/arx1 Everything is Ok')
    assert res1, "test1 FAIL"

def test_step2():
    # test2
    res1 = checkout(f'cd {folder_in}; 7z x {folder_out}/arx1 Everything is Ok')
    assert res1, "test2 FAIL"

def test_step3():
    # test3
    res1 = checkout(f'cd {folder_in}; 7z h {folder_out}/arx1 Everything is Ok')  
    assert res1, "test3 FAIL"