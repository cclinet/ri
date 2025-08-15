#include <nanobind/nanobind.h>
namespace nb = nanobind;
class Counter {
public:
  int value = 0;
  void inc() { value++; }
};

NB_MODULE(ri, m) {
  nb::class_<Counter>(m, "Counter")
      .def(nb::init<>())
      .def("inc", &Counter::inc)
      .def_ro("value", &Counter::value);
}