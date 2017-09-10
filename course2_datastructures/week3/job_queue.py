# python3
import queue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = queue.Queue()
        for job in list(map(int, input().split())):
            self.jobs.put(job)
        self.worker_job_counter = {i: 0 for i in range(self.num_workers)}
        assert m == self.jobs.qsize()

    def assign_jobs(self):
        second = 0
        while not self.jobs.empty():
            assigned = []
            while True:
                worker = self.get_free_worker()
                if worker is None:
                    break
                if not self.jobs.empty():
                    assigned.append(worker)
                    job = self.jobs.get()
                    self.worker_job_counter[worker] = job
                else:
                    break
            for assigned_worker in assigned:
                print("%d %d" % (assigned_worker, second))
            self.update_counters()
            second += 1

    def get_free_worker(self):
        for worker, counter in self.worker_job_counter.items():
            if counter == 0:
                return worker
        return None

    def update_counters(self):
        for worker, counter in self.worker_job_counter.items():
            if counter > 0:
                self.worker_job_counter[worker] = counter - 1

    def solve(self):
        self.read_data()
        self.assign_jobs()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

