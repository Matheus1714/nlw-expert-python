from barcode import Code128
from barcode.writer import ImageWriter, BinaryIO
import os

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        folder_barcodes = os.path.join(os.getcwd(), '_barcode')
        
        if not os.path.exists(folder_barcodes):
            os.makedirs(folder_barcodes)
            
        path_from_tag = os.path.join(folder_barcodes, tag.code)
        tag.save(path_from_tag)
        
        return path_from_tag

    def create_binary_barcode(self, product_code: str) -> bytes:
        barcode_binary = Code128(product_code, writer=BinaryIO())
        return barcode_binary