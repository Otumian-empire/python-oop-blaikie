import datetime


class WriteFile:

    def __init__(self, filename):
        self.file_handler = open(filename, '+a')

    def write(self, data):
        print(data, file=self.file_handler)

    def close(self):
        self.file_handler.close()


class LogFile(WriteFile):

    def write(self, data):
        data = str(datetime.datetime.now()) + " " + data
        super().write(data)


class DelimFile(WriteFile):

    def __init__(self, filename, delimiter):
        self.delimiter = delimiter
        super().__init__(filename)

    def write(self, data):
        new_data = ''
        data_size = len(data)

        self.format(data, data_size)

        for i in range(data_size):
            new_data += str(data[i])

            if i < data_size:
                new_data += self.delimiter

        super().write(new_data)

    @staticmethod
    def format(data, data_size):
        for i in range(data_size):
            if ',' in str(data[i]):
                data[i] = f'"{data[i]}"'


log = LogFile('logger.txt')
log.write('Create instance of LogFile')

delim = DelimFile('delimiter.csv', ', ')
log.write('Create instance of DelimFile')

data1 = [1, 2, 3, 4, 5]
data2 = ['poo', 'foo', 'woo', 'moo', 'ooo']
data3 = ['poo, 1', 'foo, 2', 'woo, 3', 'moo, 4', 'ooo, 5']

delim.write(data1)
log.write('Write data1 to DelimFile')

delim.write(data2)
log.write('Write data2 to DelimFile')

delim.write(data3)
log.write('Write data3 to DelimFile')

delim.close()
log.write('Close DelimFile')

log.write('Close DelimFile')
log.write('End of program')

log.close()
