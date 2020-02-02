package k8s

import "k8s.io/kubernetes1.6/staging/src/k8s.io/client-go/kubernetes"

func main() {
	kubernetes.New()
}
