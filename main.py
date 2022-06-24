import argparse;
import sys;
import banners.helpmenu as helpmenu;
import importlib;

parser = argparse.ArgumentParser(add_help=False, usage="");

def command_line(args_exist):
    if not args_exist:
        print(helpmenu.get_menu());
    
    if args_exist:
        args_setup();
        args = parser.parse_args();
        if args.help:
            print(helpmenu.get_menu());
        else:
            try:
                cipher = importlib.import_module(f"ciphers.{args.method}");
            except Exception as e:
                print(e);
                print("cipher might not exist -h for a list of cipher");
                sys.exit();
                
            if args.cipher:
                return_message = cipher.cipher(args.text, input=args.key);
                print(return_message);
                sys.exit();

            if args.decipher:
                return_message = cipher.decipher(args.text, input=args.key);
                print(return_message);
                sys.exit();



def args_setup():
    parser.add_argument("method", type=str);
    parser.add_argument("-h", "--help", dest="help", action="store_true");
    parser.add_argument("-e", "--cipher", dest="cipher", action="store_true");
    parser.add_argument("-d" "--decipher", dest="decipher", action="store_true");
    parser.add_argument("-k", "--key", nargs="?", default=None, dest="key", type=int);
    parser.add_argument("-m", "--message", dest="text", type=str);
    parser.add_argument("-i", "--interactive", dest="interactive", action="store_true");


def main():
    try:
        sys.argv[1];
    except IndexError:
        args_exist = False;
    else:
        args_exist = True;

    command_line(args_exist);

if __name__ == "__main__":
    main();
