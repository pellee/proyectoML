from database import Database
from creation import Creation
from insertandget import InsertAndGet
from mail import Email
from drive import Drive
from datetime import datetime
from script import Script


def setup_mail(to, files):
    email = Email()

    email.prepare_msg(to)
    email.attach_msg(email.set_msg(files))
    email.send_email()


def update_visibility_file(files):
    drive = Drive()
    service = drive.setup_service(drive.setup_creds())

    drive.update_visibility(service, files)


def update_data_user(emailUser, files, fileExtension):
    ig = InsertAndGet()
    filesBD = ig.get_files(emailUser)
    aux = []
    newFiles = []

    for fBD in filesBD:
        aux.append(fBD[1])

    for f in files:
        if f['id'] not in aux:
            newFiles.append(f)

    if len(newFiles) > 0:
        save_data_user(newFiles, fileExtension)
    else:
        print("THERE IS NO NEW FILES TO SAVE!")


def update_date_files(emailUser, files):
    ig = InsertAndGet()
    filesBD = ig.get_files(emailUser)

    for fBD in filesBD:
        for f in files:
            if fBD[1] == f['id']:
                aux = []
                f['modifiedTime'] = f['modifiedTime'].replace('Z', '')
                aux.append(datetime.strptime(f['modifiedTime'], '%Y-%m-%dT%H:%M:%S.%f'))
                aux.append(f['id'])
                ig.update_date_file(aux)


def save_email_user(emailUser):
    ig = InsertAndGet()

    print("SAVING USER MAIL IN DB...")
    ig.insert_user(emailUser)
    print("USER MAIL SAVED IN DB!")


def save_data_user(files, fileExtension):
    ig = InsertAndGet()

    print("SAVING USER DATA IN DB...")
    ig.insert_data_user(files, fileExtension)
    print("USER DATA SAVED IN DB!")


def verify_email(emailUser):
    ig = InsertAndGet()
    emails = ig.get_emails()

    for e in emails:
        if e == emailUser[0]:
            return True

        return False


def write_file(sharedFiles):
    st = Script()
    relativePath = r"log\logfiles.txt"

    absPath = st.join_path(relativePath)

    st.write_file(sharedFiles, absPath)


def find_public_files(files, emailUser):
    sharedFiles = []

    print("LOKING FOR PUBLIC FILES...")
    for f in files:
        if f['shared']:
            sharedFiles.append(f['name'])

    if len(sharedFiles) > 0:
        print("PUBLIC FILES FOUNDED!")
        print("CHANGING VISIBILITY OF THE FILES")
        update_visibility_file(files)
        setup_mail(emailUser[0], sharedFiles)
    else:
        print("NO PUBLIC FILES FOUNDED!")

    return sharedFiles


def setup_database():
    create = Creation()

    print("DATABASE DOESN'T EXIST")
    print("CREATING DATABASE...")
    create.create_database()
    print("CREATING PROCEDURE FOR USER...")
    create.create_proc_user()
    print("CREATING PROCEDURE FOR DATA...")
    create.create_proc_user_data()
    print("CREATING PROCEDURE FOR UPDATE DATA...")
    create.create_proc_update_data()
    print("CREATING PROCEDURE FOR GET FILES...")
    create.create_proc_get_files()
    print("CREATING PROCEDURE FOR GET USERS...")
    create.create_proc_get_users()


def get_email_user():
    drive = Drive()
    creds = drive.setup_creds()
    emailUser = []

    print("GETTING USER EMAIL")
    emailUser.append(drive.get_user_info(creds)['email'])
    print("DONE!")

    return emailUser


def get_files():
    drive = Drive()
    service = drive.setup_service(drive.setup_creds())

    print("GETTIN FILES EXTENSION")
    fileExtension = drive.get_file_extension(service)
    print("DONE!")
    print("GETTING FILES FROM GOOGLE DRIVE")
    files = drive.get_data_api(service)
    print("DONE!")

    return files, fileExtension


def main():
    db = Database()
    emailUser = get_email_user()
    (files, fileExtension) = get_files()

    if not db.exist_database():
        setup_database()
    else:
        print("DATABASE ALREADY EXIST!")

    sharedFiles = find_public_files(files, emailUser)
    write_file(sharedFiles)

    (files, fileExtension) = get_files()

    if verify_email(emailUser):
        print("EXISTING USER!")

        print("CHECKING IF THERE ARE NEW FILES...")
        update_data_user(emailUser, files, fileExtension)
        print("UPDATING DATE FILE...")
        update_date_files(emailUser, files)
        print("DATE UPDATED!")

    else:
        print("NEW USER!")
        save_email_user(emailUser)
        save_data_user(files, fileExtension)


if __name__ == '__main__':
    main()
