// gcc ./listy.c -m32 -o listy -lpthread

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

#define MAXTHREADS 2

typedef struct _Node {
    struct _Node* next;
    char* content;
} Node;

Node* head = NULL;

// A really bad thread pool implmementation...
char task_data[MAXTHREADS][128];
pthread_t threads[MAXTHREADS];
char running[MAXTHREADS];

// TODO remove this
void printflag() {
    system("cat flag.txt");
}

void readline(char* buf, int n, FILE* in) {
    fgets(buf, n, in);
    buf[strcspn(buf, "\n")] = 0; // strip newline
}

void *add_task(void* id) {
    int threadid = (int) id;
    char* data = task_data[threadid];
    printf("Adding node with %s (thread %d)\n",data,threadid);
    sleep(1); // look like we're hard at work
    printf("Adding done! (thread %d)\n",threadid);
    Node* n = malloc(sizeof(Node));
    n->content = strdup(data);
    n->next = head;
    head = n;
    running[threadid] = 0;
}

void *remove_task(void* id) {
    int threadid = (int) id;
    char* data = task_data[threadid];
    int index = 0;
    if (!sscanf(data,"%d",&index)) {
        return;
    }
    printf("Removing node %d (thread %d)\n",index,threadid);
    if (!head) {
        printf("Empty list!\n");
        return;
    }
    if (index < 0) {
        printf("Invalid index!\n");
        return;
    }
    if (!index) {
        Node* tmp = head->next;
        free(head);
        head = tmp;
    } else {
        index--;
        Node* prev = head;
        while (index > 0) {
            if (!prev) {
                printf("Invalid index!\n");
                return;
            }
            prev = prev->next;
            index--;
        }
        if (!prev || !prev->next) {
            printf("Invalid index!\n");
            return;
        }
        Node* next = prev->next->next;
        sleep(1); // look like we're hard at work
        Node* cur = prev->next;
        prev->next = next;
        free(cur);
    }
    printf("Removing done! (thread %d)\n",threadid);
    running[threadid] = 0;
}

void *update_task(void* id) {
    int threadid = (int) id;
    char* data = task_data[threadid];
    int index = 0;
    char new[128];
    if (sscanf(data,"%d;%s",&index,new) != 2) {
        return;
    }
    printf("Updating node %d with %s (thread %d)\n",index,new,threadid);
    if (index < 0) {
        printf("Invalid index!\n");
        return;
    }
    Node* cur = head;
    while (index > 0) {
        if (!cur) {
            printf("Invalid index!\n");
            return;
        }
        cur = cur->next;
        index--;
    }
    if (!cur) {
        printf("Invalid index!\n");
        return;
    }
    sleep(1); // look like we're hard at work
    if (strlen(new) > strlen(cur->content)) {
        free(cur->content);
        cur->content = strdup(new);
    } else { // just reuse the space we have
        strcpy(cur->content,new);
    }
    printf("Updating done! (thread %d)\n",threadid);
    running[threadid] = 0;
}

void addnode() {
    printf("Send strings to add, one on each line.\n");
    printf("Send an empty line to finish.\n");
    char line[128];
    while (1) {
        readline(line, sizeof(line), stdin);
        if (!strlen(line)) {
            break;
        }
        int i = 0;
        while (1) {
            if (!running[i]) {
                running[i] = 1;
                strncpy(task_data[i], line, 128);
                pthread_create(&threads[i], NULL, add_task, (void*) i);
                break;
            }
            usleep(10000);
            i = (i+1) % MAXTHREADS;
        }
    }
}

void removenode() {
    printf("Send index to remove, one on each line.\n");
    printf("Send an empty line to finish.\n");
    char line[128];
    while (1) {
        readline(line, sizeof(line), stdin);
        if (!strlen(line)) {
            break;
        }
        int i = 0;
        while (1) {
            if (!running[i]) {
                running[i] = 1;
                strncpy(task_data[i], line, 128);
                pthread_create(&threads[i], NULL, remove_task, (void*) i);
                break;
            }
            usleep(10000);
            i = (i+1) % MAXTHREADS;
        }
    }
}

void updatenode() {
    printf("Send index and new string in the format index;new.\n");
    printf("Send an empty line to finish.\n");
    char line[128];
    while (1) {
        readline(line, sizeof(line), stdin);
        if (!strlen(line)) {
            break;
        }
        int i = 0;
        while (1) {
            if (!running[i]) {
                running[i] = 1;
                strncpy(task_data[i], line, 128);
                pthread_create(&threads[i], NULL, update_task, (void*) i);
                break;
            }
            usleep(10000);
            i = (i+1) % MAXTHREADS;
        }
    }
}

void printlist() {
    Node* cur = head;
    int i = 0;
    while (cur != NULL) {
        printf("%d: %s\n",i,cur->content);
        i++;
        cur = cur->next;
    }
}

int main(int argc, const char* argv[]) {
    setbuf(stdout, NULL);
    printf("Commands:\n"
           "\n"
           "add: Add item to beginning of list.\n"
           "remove: Delete item in list.\n"
           "update: Update item in list.\n"
           "print: Print list.\n"
           "quit: Quit the program.\n");
    char line[512];
    while (1) {
        printf("> ");
        readline(line, sizeof(line), stdin);
        if (!strcmp(line,"add")) {
            addnode();
        } else if (!strcmp(line,"remove")) {
            removenode();
        } else if (!strcmp(line,"update")) {
            updatenode();
        } else if (!strcmp(line,"print")) {
            printlist();
        } else if (!strcmp(line,"quit")) {
            break;
        } else {
            printf("Invalid command.\n");
        }
    }
}
