
# KuberDock - is a platform that allows users to run applications using Docker
# container images and create SaaS / PaaS based on these applications.
# Copyright (C) 2017 Cloud Linux INC
#
# This file is part of KuberDock.
#
# KuberDock is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# KuberDock is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KuberDock; if not, see <http://www.gnu.org/licenses/>.

from .container import KuberDock
from ..helper import make_config


def parser(subs):
    container = subs.add_parser('kuberdock')
    container.set_defaults(call=wrapper)
    action = container.add_subparsers(help="Action", title="Target actions",
                                      description="Valid actions for targets",
                                      dest="action")

    c_create = action.add_parser('create')
    c_create.add_argument('name', help="Container name")

    c_create.add_argument('-C', '--container', dest='image',
                          help="Image to take action upon")
    c_create.add_argument(
        '--index', default=0, type=int,
        help="Index of ports or volumes entry (by default 0)")
    c_create.add_argument(
        '--container-port',
        help="Add or change a container port of ports entry.")
    c_create.add_argument(
        '--mount-path',
        help="Point to existent mount path entry or create a new one")
    c_create.add_argument(
        '--kubes', type=int,
        help="Set image kubes. Integer between 1 and 10",
        default=1)
    c_create.add_argument('--kube-type', help="Set pod kube type")
    c_create.add_argument('--restart-policy', default="Always",
                          help="Set container restart policy",
                          dest="restartPolicy",
                          choices=['Always', 'Never', 'OnFailure'])
    c_create.add_argument('--env', help="Add or change environment variables")
    c_create.add_argument('-p', '--persistent-drive',
                          help="Specify persistent drive for mount path")
    c_create.add_argument('-s', '--size', type=int,
                          help="Specify size in GB for drive to be created")

    c_set = action.add_parser('set')
    c_set.add_argument('name', help="Container name")

    c_set.add_argument('-C', '--container', dest='image',
                       help="Image to take action upon")
    c_set.add_argument('-d', '--delete', help="Delete image from a container")
    c_set.add_argument('--index', default=0, type=int,
                       help="Index of ports or volumes entry (by default 0)")
    c_set.add_argument('--container-port',
                       help="Add or change a container port of ports entry")
    c_set.add_argument(
        '--mount-path',
        help="Point to existent mount path entry or create a new one")
    c_set.add_argument('--kubes', help="Set image kubes", default=1)
    c_set.add_argument('--kube-type', help="Set pod kube type")
    c_set.add_argument('--restart-policy', default="Always",
                       help="Set container restart policy",
                       dest="restartPolicy",
                       choices=['Always', 'Never', 'OnFailure'])
    c_set.add_argument('--env', help="Add or change environment variables")
    c_set.add_argument('-p', '--persistent-drive',
                       help="Specify persistent drive for mount path")
    c_set.add_argument('-s', '--size', type=int,
                       help="Specify size in GB for drive to be created")
    c_set.add_argument(
        '--delete-env',
        help="Delete comma-separated list of "
             "environment variables from pending container")
    c_set.add_argument('--list-env', action='store_true',
                       help="List environment variables of pending container")

    c_del = action.add_parser('delete')
    c_del.add_argument('name', help="Container name")

    c_start = action.add_parser('start')
    c_start.add_argument('name', help="Container name")

    c_stop = action.add_parser('stop')
    c_stop.add_argument('name', help="Container name")

    c_start = action.add_parser('save')
    c_start.add_argument('name', help="Container name")

    c_forget = action.add_parser('forget')
    c_forget.add_argument('name', nargs='?', default='',
                          help="Container name to forget")

    c_search = action.add_parser('search')
    c_search.add_argument('search_string', help="Search string")
    c_search.add_argument('-p', '--page', default=1, type=int,
                          help="Page to display")
    c_search.add_argument(
        '-R', '--registry',
        help="Registry to search in. By default dockerhub is used")

    c_image_get = action.add_parser('image_info')
    c_image_get.add_argument('image', help="Image name")

    action.add_parser('list')
    # c_list = action.add_parser('list')

    # c_kubes = action.add_parser('kube-types')
    action.add_parser('kube-types')

    c_drive = action.add_parser('drives')
    pdrive = c_drive.add_subparsers(
        help="Persistent Drive Action",
        title="Drive actions",
        description="Valid actions for persistent drives",
        dest="pdaction")
    add_drive = pdrive.add_parser('add')
    add_drive.add_argument('name', help="Name of a drive to be added")
    add_drive.add_argument('--size', required=True,
                           help="Size in GB of a drive to be added")
    pdrive.add_parser('list')
    delete_drive = pdrive.add_parser('delete')
    delete_drive.add_argument('name', help="Name of a drive to delete")

    c_desc = action.add_parser('describe')
    c_desc.add_argument('name', help="Container name")


def wrapper(data):
    args = make_config(data)
    container = KuberDock(**args)
    getattr(container, args.get('action', 'get').replace('-', '_'), 'get')()
