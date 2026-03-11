# Ransomware Idendification

## Setup instructions
1. run the server
```bash
cd api
uvicorn api:main --reload
```

## API Endpoints
Predict the fake login requests.
Request Body (JSON):
```bash
 {
  {
  "EntryPoint": 0,
  "magic_number": 0,
  "bytes_on_last_page": 0,
  "pages_in_file": 0,
  "relocations": 0,
  "size_of_header": 0,
  "min_extra_paragraphs": 0,
  "max_extra_paragraphs": 0,
  "init_ss_value": 0,
  "init_sp_value": 0,
  "init_ip_value": 0,
  "init_cs_value": 0,
  "over_lay_number": 0,
  "oem_identifier": 0,
  "address_of_ne_header": 0,
  "SizeOfCode": 0,
  "SizeOfInitializedData": 0,
  "SizeOfUninitializedData": 0,
  "AddressOfEntryPoint": 0,
  "BaseOfCode": 0,
  "BaseOfData": 0,
  "ImageBase": 0,
  "SectionAlignment": 0,
  "FileAlignment": 0,
  "OperatingSystemVersion": 0,
  "ImageVersion": 0,
  "SizeOfImage": 0,
  "SizeOfHeaders": 0,
  "Checksum": 0,
  "SizeofStackReserve": 0,
  "SizeofStackCommit": 0,
  "SizeofHeapCommit": 0,
  "SizeofHeapReserve": 0,
  "LoaderFlags": 0,
  "text_VirtualSize": 0,
  "text_VirtualAddress": 0,
  "text_SizeOfRawData": 0,
  "text_PointerToRawData": 0,
  "text_PointerToRelocations": 0,
  "text_PointerToLineNumbers": 0,
  "rdata_VirtualSize": 0,
  "rdata_VirtualAddress": 0,
  "rdata_SizeOfRawData": 0,
  "rdata_PointerToRawData": 0,
  "rdata_PointerToRelocations": 0,
  "rdata_PointerToLineNumbers": 0,
  "registry_read": 0,
  "registry_write": 0,
  "registry_delete": 0,
  "network_threats": 0,
  "network_dns": 0,
  "network_http": 0,
  "network_connections": 0,
  "processes_monitored": 0,
  "files_text": 0,
  "files_unknown": 0,
  "dlls_calls": 0,
  "apis": 0,
  "encryption_score": 0,
  "system_modification_score": 0
}
}
```

Prediction 0: normal
Prediction 1: Ransomware