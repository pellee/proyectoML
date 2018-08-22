import os
import datetime


class Script:

    def read_script(self, pathsql):
        file = open(pathsql, 'r')
        fileReaded = file.read()
        file.close()

        sqlcomm = fileReaded.replace('\n', '').split(';')[:-1]

        aux = []

        for a in sqlcomm:
            a = a.replace("delimiter", ' ')
            a = a.replace("$$", ' ')
            a = a.replace("BEGIN", ' ')
            a = a.replace("END", ' ')

            aux.append(a)

        return aux

    def join_path(self, relativePath):
        proyectPath = os.path.dirname(__file__)
        absPath = os.path.join(proyectPath, relativePath)

        return absPath

    def write_file(self, sharedFiles, path):
        f = open(path, "a+")

        try:
            now = datetime.datetime.now()
            for sf in sharedFiles:
                f.write(sf)
                f.write("   ")
                f.write(str(now))
                f.write("\n")
        except Exception as e:
            print(e)
        finally:
            f.close()
