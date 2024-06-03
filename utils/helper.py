import os


def save_credentials(account_id, password, seed):
    with open(f"creds/{account_id}.txt", "w+") as f:
        f.write(account_id + "\n")
        f.write(password + "\n")
        f.write(" ".join(seed))


def generate_new_account_id(account_id):
    cur_file_path = os.path.abspath(__file__)
    target_dir = os.path.dirname(cur_file_path).split("/")[:-1]
    target_dir.append("creds")
    target_dir = "/".join(target_dir)

    file_names = []
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_names.append(file.split(".")[0])
    while account_id in file_names:
        next_num = int(account_id[-1]) + 1
        new_account_id = account_id[:-1] + str(next_num)
        account_id = new_account_id
    return account_id


def get_passphrase(account_id):
    cur_file_path = os.path.abspath(__file__)
    target_dir = os.path.dirname(cur_file_path).split("/")[:-1]
    target_dir.append("creds")
    target_dir.append(account_id + ".txt")
    target_file = "/".join(target_dir)
    with open(target_file, "r") as f:
        lines = f.readlines()
        return lines[-1]

if __name__ == "__main__":
    print(get_passphrase("coursetest2"))
