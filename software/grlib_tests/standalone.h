#ifndef STANDALONE_H
#define STANDALONE_H

void report_start(void);
void report_end(void);
void report_device(int dev);
void report_subtest(int test);
void fail(int dev);
char *dev_to_string(unsigned int dev);
char *dev_to_subtest(int dev, int test);

#endif
