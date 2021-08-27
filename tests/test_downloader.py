
import unittest
import tempfile
import os
import argopandas.downloader as dl


class TestDownloader(unittest.TestCase):

    def test_prefix(self):
        self.assertEqual(dl._common_prefix([]), '')
        self.assertEqual(dl._common_prefix(['apple']), 'apple')
        self.assertEqual(dl._common_prefix(['apple', 'banana']), '')
        self.assertEqual(dl._common_prefix(['apple', 'apple']), 'apple')
        self.assertEqual(dl._common_prefix(['apple', 'animal']), 'a')

    def test_init_message(self):
        self.assertEqual(dl._init_message([]), None)
        self.assertEqual(dl._init_message(['fish']), "Downloading 'fish'")
        self.assertEqual(dl._init_message(['p/a', 'p/b']), "Downloading 2 files from 'p'")
        self.assertEqual(dl._init_message(['apple', 'banana']), "Downloading 2 files")

    def test_download_one(self):
        with tempfile.TemporaryDirectory() as temp:
            dl.download_one('https://httpbin.org/get', os.path.join(temp, 'get.json'), quiet=True)
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get.json')))

            dl.download_one('https://httpbin.org/get', os.path.join(temp, 'get2.json'), quiet=False)
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get2.json')))

            # overwrites get2.json
            dl.download_one('https://httpbin.org/status/200', os.path.join(temp, 'get2.json'), quiet=False)
            with open(os.path.join(temp, 'get2.json'), 'rb') as f:
                self.assertEqual(f.read(), b'')

    def test_download_sequential(self):
        self.assertEqual(dl.download_sequential([]), [])
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(
                dl.download_sequential([
                    ('https://httpbin.org/get', os.path.join(temp, 'get.json'))
                ]),
                []
            )
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get.json')))
            os.unlink(os.path.join(temp, 'get.json'))

            self.assertEqual(
                dl.download_sequential([
                    ('https://httpbin.org/get', os.path.join(temp, 'get.json')),
                    ('https://httpbin.org/status/200', os.path.join(temp, 'get2.json'))
                ]),
                []
            )
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get.json')))
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get2.json')))

            errors = dl.download_sequential([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json'))
            ])
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], 0)
            self.assertRegex(errors[0][1], '404')

            errors = dl.download_sequential([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json')),
                ('https://httpbin.org/status/200', os.path.join(temp, 'get2.json'))
            ])
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], 0)
            self.assertRegex(errors[0][1], '404')

            errors = dl.download_async([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json')),
                ('https://httpbin.org/status/404', os.path.join(temp, '4042.json'))
            ], max_errors=1)
            self.assertEqual(len(errors), 1)

    def test_download_async(self):
        self.assertEqual(dl.download_async([]), [])
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(
                dl.download_async([
                    ('https://httpbin.org/get', os.path.join(temp, 'get.json'))
                ]),
                []
            )
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get.json')))
            os.unlink(os.path.join(temp, 'get.json'))

            self.assertEqual(
                dl.download_async([
                    ('https://httpbin.org/get', os.path.join(temp, 'get.json')),
                    ('https://httpbin.org/status/200', os.path.join(temp, 'get2.json'))
                ]),
                []
            )
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get.json')))
            self.assertTrue(os.path.isfile(os.path.join(temp, 'get2.json')))

            errors = dl.download_async([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json'))
            ])
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], 0)
            self.assertRegex(errors[0][1], '404')

            errors = dl.download_async([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json')),
                ('https://httpbin.org/status/200', os.path.join(temp, 'get2.json'))
            ])
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0][0], 0)
            self.assertRegex(errors[0][1], '404')

            errors = dl.download_async([
                ('https://httpbin.org/status/404', os.path.join(temp, '404.json')),
                ('https://httpbin.org/status/404', os.path.join(temp, '4042.json'))
            ], max_errors=1)
            self.assertEqual(len(errors), 1)


if __name__ == '__main__':
    unittest.main()
