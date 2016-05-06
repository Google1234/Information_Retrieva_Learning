
'''
BSBI NDEXConSTRUCTION()
n <- 0
while(all documents have not been processed)
    do n<-n+1
        block <- PARSENEXTBLOCK()    //文档分析
        BSBI-INVERT(block)
        WRITEBLOCKTODISK(block,fn)
MERGEBLOCKS(f1,...,fn;fmerged)
'''