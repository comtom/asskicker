from japronto import Application
from hashlib import sha512

def throughput(request):
    return request.Response(text='{"throughput":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in ipsum a velit faucibus tempor vel nec odio. Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur quis orci eget purus tempus aliquet eu eu risus. Ut velit elit, viverra et ex vel, scelerisque rhoncus odio. Donec vitae diam pellentesque, commodo velit et, lacinia leo. In vel pharetra purus, sed eleifend nunc. Maecenas porta rhoncus consectetur. In hac habitasse platea dictumst. Duis sed erat nibh. Morbi imperdiet lorem purus, vitae facilisis enim maximus et. Phasellus ullamcorper sapien eget neque eleifend malesuada."}')


def cpu(request):
    hash_value = b'Sparkers doing some benchmarking'
    for _ in range(256):
        hash_value = sha512(hash_value).digest()

    return request.Response(text='{"Hashed":"%s"}' % hash_value)


def ram(request):
    return request.Response(text='{"n_vowels":1234}')


def disk(request):
    return request.Response(text='{"bytes":1234}')


app = Application()
app.router.add_route('/throughput', throughput)
app.router.add_route('/cpu', cpu)
app.router.add_route('/ram', ram)
app.router.add_route('/disk', disk)
app.run(debug=False)
