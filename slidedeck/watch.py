import os
import sys
import time
from slidedeck.render import process_slides

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    print('#'*78)
    print('The watch command requires that you install the python package "watchdog"')
    print('for monitoring filesystem events. You can obtain the package with\n')
    print('$ sudo easy_install watchdog')
    print('')
    print('Or download it from https://pypi.python.org/pypi/watchdog')
    print('#'*78)
    sys.exit(1)


def watch_project(markdown_fn, output_fn, template_fn, render_first=True):
    class Handler(FileSystemEventHandler):
        def on_any_event(self, event):
            if event.src_path == os.path.abspath(output_fn):
                return
            print('Rendering slides...')
            process_slides(markdown_fn, output_fn, template_fn)

    if render_first == True:
        process_slides(markdown_fn, output_fn, template_fn)
        
    observer = Observer()
    event_handler = Handler()

    dirname = os.path.dirname(os.path.abspath(markdown_fn))
    
    observer.schedule(event_handler, path=dirname, recursive=True)
    print("Watching for events on {:s}...".format(dirname))
    observer.start()

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    watch_project(os.path.abspath('f'), None, None)
