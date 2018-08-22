from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from apiclient import errors
from apiclient.http import MediaFileUpload
from script import Script


class Drive:

    def get_user_info(self, credentials):
        user_info_service = build(serviceName='oauth2', version='v2',
                                  http=credentials.authorize(Http()))
        user_info = None
        try:
            user_info = user_info_service.userinfo().get().execute()
        except errors.HttpError as e:
            logging.error('An error occurred: %s', e)
        if user_info and user_info.get('id'):
            return user_info
        else:
            raise NoUserIdException()

    def setup_creds(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                  'https://www.googleapis.com/auth/userinfo.email',
                  'https://www.googleapis.com/auth/drive.metadata',
                  'https://www.googleapis.com/auth/drive']
        relativePath = r"clientAndToken\token.json"
        sp = Script()
        absPath = sp.join_path(relativePath)
        store = oauth_file.Storage(absPath)
        creds = store.get()
        if not creds or creds.invalid:
            relativePath = r"clientAndToken\client_secret.json"
            absPath = sp.join_path(relativePath)
            flow = client.flow_from_clientsecrets(absPath, SCOPES)
            creds = tools.run_flow(flow, store)

        return creds

    def setup_service(self, creds):
        service = build('drive', 'v3', http=creds.authorize(Http()))

        return service

    def get_file_extension(self, service):
        results = service.files().list(pageSize=10, fields="nextPageToken, files(fullFileExtension)").execute()
        itemEx = results.get('files', [])

        return itemEx

    def get_data_api(self, service):
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name, owners, modifiedTime, shared, fullFileExtension, permissions)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files founded!')

        return items

    def update_visibility(self, service, files):
        try:
            for f in files:
                if f['shared']:
                    up = service.permissions().delete(
                        fileId=f['id'], permissionId=f['permissions'][0]['id']).execute()
        except Exception as e:
            print(e)
