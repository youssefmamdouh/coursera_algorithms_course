# python3
from queue import PriorityQueue


class JobQueue:
    def read_data(self):
        self.num_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.workers = PriorityQueue()
        [self.workers.put((0, i)) for i in range(self.num_workers)]
        self.worker_job = []
        self.job_seconds = []

    def assign_jobs(self):
        for i in range(self.m):
            free_worker = self.workers.get()
            self.worker_job.append(free_worker[1])
            self.job_seconds.append(free_worker[0])
            self.workers.put((free_worker[0] + self.jobs[i], free_worker[1]))

    def print_schedule(self):
        for i in range(self.m):
            print(self.worker_job[i], self.job_seconds[i])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.print_schedule()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
