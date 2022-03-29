import qrcode

def get_qrcode(url='http://google.com', name='t.n.o'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open the {name}.png'

def main():
    print(get_qrcode(url='https://github.com/tursunovn', name='github'))
    print(get_qrcode(url='https://www.youtube.com/channel/UC2Fd_VAfw_5G7PQWulXwjZw', name='Excel_Group'))

if __name__ == '__main__':
    main()