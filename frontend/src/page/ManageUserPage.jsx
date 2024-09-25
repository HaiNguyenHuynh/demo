import { useQuery } from "@tanstack/react-query";
import React, { useState } from "react";
import { fetchAllUser, fetchAllUserById } from "../api/services";
import Modal from "../components/Modal";
import ModalAddUser from "../components/ModalAddUser";
import { useParams } from "react-router-dom";

export default function ManageUserPage() {
  const param = useParams();
  const checkPram = Object.keys(param).length > 0;
  const [isOpenModalAdd, setisOpenModalAdd] = useState(false);
  const [isOpenModalEdit, setisOpenModalEdit] = useState(false);
  const [isOpenModalDelete, setIsOpenModalDelete] = useState(false);
  const [userSelected, setUserSelected] = useState();
  const { data, isLoading } = useQuery({
    queryKey: ["allUser"],
    queryFn: fetchAllUser,
    enabled: Object.keys(param).length === 0,
  });

  const { data: dataById, isLoading: loadingById } = useQuery({
    queryKey: ["UserID", param?.id],
    queryFn: () => fetchAllUserById(param?.id),
    enabled: param?.id?.length > 0,
  });

  return isLoading || loadingById ? (
    <div>...Loading</div>
  ) : (
    <div className="p-5">
      {!checkPram && (
        <button
          onClick={() => setisOpenModalAdd(true)}
          className="bg-blue-400 text-white py-1 px-3 rounded-[100px]"
        >
          Create user
        </button>
      )}
      <div className="relative flex flex-col w-full h-full  text-gray-700 bg-white shadow-md rounded-xl bg-clip-border mt-5">
        <table className="w-full text-left table-auto min-w-max">
          <thead>
            <tr>
              <th className="p-4 border-b border-blue-gray-100 bg-blue-gray-50">
                <p className="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                  ID
                </p>
              </th>
              <th className="p-4 border-b border-blue-gray-100 bg-blue-gray-50">
                <p className="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                  Name
                </p>
              </th>
              <th className="p-4 border-b border-blue-gray-100 bg-blue-gray-50">
                <p className="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                  Age
                </p>
              </th>
              <th className="p-4 border-b border-blue-gray-100 bg-blue-gray-50">
                <p className="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">
                  Action
                </p>
              </th>
            </tr>
          </thead>
          {!data && !dataById && (
            <div className="absolute left-1/2 mt-5 -translate-x-1/2 font-semibold">
              No Data
            </div>
          )}

          <tbody>
            {checkPram && dataById && (
              <tr key={dataById?.id}>
                <td className="p-4 border-b border-blue-gray-50">
                  <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                    {dataById?.id}
                  </p>
                </td>
                <td className="p-4 border-b border-blue-gray-50">
                  <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                    {dataById?.name}
                  </p>
                </td>
                <td className="p-4 border-b border-blue-gray-50">
                  <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                    {dataById?.age}
                  </p>
                </td>
                <td className="p-4 border-b border-blue-gray-50">
                  <div className="flex items-center gap-2">
                    <button className="block font-sans text-sm antialiased font-medium leading-normal text-blue-gray-900">
                      Edit
                    </button>
                    <button
                      onClick={() => setIsOpenModalDelete(true)}
                      className="block font-sans text-sm antialiased font-medium leading-normal text-blue-gray-900"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            )}

            {!checkPram &&
              data &&
              data.map((val) => (
                <tr key={val.id}>
                  <td className="p-4 border-b border-blue-gray-50">
                    <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                      {val?.id}
                    </p>
                  </td>
                  <td className="p-4 border-b border-blue-gray-50">
                    <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                      {val?.name}
                    </p>
                  </td>
                  <td className="p-4 border-b border-blue-gray-50">
                    <p className="block font-sans text-sm antialiased font-normal leading-normal text-blue-gray-900">
                      {val?.age}
                    </p>
                  </td>
                  <td className="p-4 border-b border-blue-gray-50">
                    <div className="flex items-center gap-2">
                      <button className="block font-sans text-sm antialiased font-medium leading-normal text-blue-gray-900">
                        Edit
                      </button>
                      <button
                        onClick={() => setIsOpenModalDelete(true)}
                        className="block font-sans text-sm antialiased font-medium leading-normal text-blue-gray-900"
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
          </tbody>

          <div className="absolute left-1/2 mt-5 -translate-x-1/2 font-semibold">
            No Data
          </div>
        </table>
      </div>

      {isOpenModalDelete && (
        <Modal handleClose={() => setIsOpenModalDelete(false)} />
      )}

      {isOpenModalAdd && (
        <ModalAddUser handleClose={() => setisOpenModalAdd(false)} />
      )}
    </div>
  );
}
