set -e
cd "$(dirname "$0")"
python3 build_ld.py && python3 build_texts.py && python3 build_pages.py && python3 build_pages2.py
python3 build_v2.py
