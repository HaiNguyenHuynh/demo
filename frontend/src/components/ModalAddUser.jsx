import { useMutation, useQueryClient } from "@tanstack/react-query";
import React, { useState } from "react";
import { createUser } from "../api/services";

export default function ModalAddUser({ handleClose }) {
  const queryClient = useQueryClient();
  const [name, setName] = useState();
  const [age, setAge] = useState();
  const { mutate, isLoading } = useMutation({
    mutationKey: "addUser",
    mutationFn: () => createUser({ name, age }),
    onSuccess: () => {
      queryClient.invalidateQueries("allUser");
      setName("");
      setAge("");
    },
  });
  const handleAddUser = (e) => {
    if (!name || !age) {
      alert("some fields are empty");
      return;
    }
    mutate();
  };
  return (
    <div>
      <div
        class="relative z-10"
        aria-labelledby="modal-title"
        role="dialog"
        aria-modal="true"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          aria-hidden="true"
        ></div>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <div class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div className="mb-4 text-xl font-semibold">Create user</div>
                <div class="sm:flex sm:items-start">
                  <div className="w-full">
                    <div
                      className="space-y-3"
                      onSubmit={(e) => {
                        e.preventDefault();
                      }}
                    >
                      <div>
                        <label
                          htmlFor="email"
                          className="block text-sm font-medium leading-6 text-gray-900"
                        >
                          Name
                        </label>
                        <div className="mt-2">
                          <input
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            required
                            className="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                          />
                        </div>
                      </div>

                      <div>
                        <div className="flex items-center justify-between">
                          <label
                            htmlFor="password"
                            className="block text-sm font-medium leading-6 text-gray-900"
                          >
                            Age
                          </label>
                        </div>
                        <div className="mt-2">
                          <input
                            value={age}
                            onChange={(e) => setAge(e.target.value)}
                            type="number"
                            required
                            className="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                          />
                        </div>
                      </div>
                      <div class="flex pt-5 items-end justify-end">
                        <button
                          onClick={handleClose}
                          type="button"
                          class="mt-3  min-w-[100px] inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                        >
                          Cancel
                        </button>
                        <button
                          type="button"
                          onClick={(e) => handleAddUser(e)}
                          class="inline-flex w-full justify-center rounded-md min-w-[100px] bg-blue-500 px-3 py-2 text-sm font-semibold text-white shadow-sm sm:ml-3 sm:w-auto"
                        >
                          Save
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
